title: Basics of Email Threading and Other Lessons from Building a SMS-Email Relay
date: 2020-08-19
category: solution overview
tags: email, email threading

One of my projects during the last year was building a set of microservices  that sent text messages based on events as well as relay SMS replies to the right agent or agent group. The goal was to increase the quality of communication between our agents and drivers by moving it from calls, which can often be inconvenient and misheard, to SMS, which has the advantages of being asynchronous and exact. We decided to use an email relay since email was the key technology we could easily tap into. 

This post outlines the design of this SMS-email system, highlighting the design challenges presented by email threading, and ending with a short reflection on microservices.

I’m a developer and sometime project manager in the logistics industry. Most employees at my company work in operations, which involves coordinating between facilities, truck drivers, and truck dispatchers. There is a big movement towards “visibility” -- Amazon-style real-time tracking -- in the industry, but we often relied on phone calls for updates. These calls are often viewed as a hassle and depending on the quality of the connection or a language barrier, may not lead to the desired update. Based on this feedback, we decided to build a set of microservices to shift from calls to text messages. A long-term goal is to move communication and order information into a single tool, but this was not possible with our current third-party system. We decided to make replies to the SMS go to email, the agents’ other primary tool.

The general sequence of communication was:
An automated text message was sent to the driver based on an event. The message could include reference numbers or ask for an update if there wasn’t recent communication.
The driver replies to the text message. The message goes through a service to a webhook. This is added to a queue for emailing to the proper agent.
The agent replies to the driver’s message via email. A microservice checks a dedicated account for new replies. When found, the message is sent as a SMS to the driver’s phone number.

The automated text messages were sent based on information in the database. The event log provided the information needed to trigger a message. Other messages were based on an order being in a status for a period of time, which could be found by a query.

Messages arrived via a webhook. The metadata from the vendor included the sender (driver) phone number and the tag of the agent group associated with the receiving phone number. The sender number was used to look up the order number and the agent group. If there was no recent number associated with the order, the message was sent to the tagged agent group. To help with email organization, the subject included the order number and name. 

Emails were sent by a dedicated account, and agents could reply to the text message by replying to the email. A service checked the dedicated account for new messages. The order number is used to look-up the driver phone number, and the system replied if nothing could be found. 

The main challenges of the project involved email threading and the context it provides. In the first version of the service, agents received a new email each time a driver message was relayed, so agents would look back at older messages for the context of the message. If the most recent message was automated, the context was lost to them. 

Email threading is more complex than looking at the subject, as I naively assumed it would do. Email is nothing like a database -- there’s no primary or foregin key to organize the messages -- and there’s no way it could be outside a closed system. The sending system assigns and attaches an ID to the email, but these are generated independently for each account. Threading is done by this algorithm, which considers several pieces of email metadata (“headers”) hidden from users.

The ID assigned by the sender is sent in the `Message-Id` field. When replying, the `Message-Id` is moved to the `In-Reply-To` field. Using these two pieces of data, threading in the simple scenario of two accounts replying back-and-forth is straightforward and analogous to a linked-list.

Lived experience has many complex scenarios: one person replying to the same email twice, two people replying to the same email, people removed from the chain, the chain branching. These are organized using `References`, which is a string of the proceeding `Message-Id`’s. Using these fields, parent and child messages can be identified, and the messages organized in an UI. 

Learning all this, the solution was clear: the sent messages needed to include these missing headers. One solution was to look-up the last message in the thread and reply to it. Since messages included a reference number, they could be identified with a search operation.

Making the automated messages referenceable by agents required storing it. Emails could be sent to the agent in parallel with the text message to the driver. This would decrease efficiency as agents would open messages needlessly. The information needed to be made available just-in-time. Our system has a notes feature, a possible place to log the communication. Since agents are in the system, looking up an order and viewing notes is part of their workflow. Ideally, the information would be closer-at-hand than this. We opted to solve the email metadata issue and the automated message issue using a simple fact table.

The fact table stores the last `Message-Id`, `References`, and text message sent. Values in the fact table are updated when an email-to-relay is received or a text message sent. Looking-up the stored values had little marginal cost since there was an existing query to lookup the appropriate agent. There’s a performance cost to all the database operations, connecting having the longest time. As the application scales, batch jobs will be more appropriate. Alternatively, using asynchronous database connections may be possible.

As I worked on this and similar projects while reading and learning more about modern software development, I came to appreciate the values underpinning microservice architecture. Decoupling allows for development of small, focused applications that can be easily refactored. While not necessarily meeting the standard of a microservice, a cron job is often Good Enough when starting out. Google, Airbnb, and Pinterest all built their scheduling and triggering systems because they had too many cron jobs. On the other end, having a webhook that can trigger actions provides considerable value as it’s no longer about what information you’re sending, but what information you’re receiving and can put to use.

