# 🚀 Transitioning to KX: Exploring a Series of Use Cases 

Migration projects are often challenging. Beyond the unexpected technical challenges that may arise during the process, new technologies can spark reluctance among individuals within the organization. In the case of kdb+ as a new technology for time series databases, the most prominent criticisms I've encountered have been:

- 💰 **Licensing costs**: It's very expensive,
- 📉 **Lack of performance metrics**: Vendor-published benchmarks are rare or biased,
- 🤯 **Difficult to learn**: kdb+ is very complicated,
- 💻 **Support for adoption**: There is a lack of professionals specialized in kdb+

Despite these criticisms —many of which are often unfounded— the organization moved forward with the transition to KX. In my view, this was a wise, long-term decision. I’d like to share my experience working on this migration project so far:

When migrating tick data to kdb+, one of the more straightforward aspects is handling raw trade and quote data. This is because such data can often be re-sourced from market data providers. Therefore, the main focus during migration lies in rethinking the architecture of the data analytics platform itself.

By shifting to the kdb+ times series database, teams can take full advantage of its performance and expressiveness, among other powerful features. This transition also enables seamless integration with existing Python-based analytics platforms through PyKX, resulting in a more flexible and scalable architecture.

It's well known that the syntactic style of kdb+/q can be difficult for newbies. Additionally, as a niche technology, LLMs are currently less effective in assisting with it compared to more mainstream languages like Python, due to limited training data. However, I found the KX community to be highly supportive—responsive to both simple and complex questions alike. Gaining full understanding and control over your work has a cost today, but in the end, mastering it is well worth the effort. After all, real-time applications still require a significant amount of human support.

Over the coming days, I will showcase a series of use cases that will help you understand the basics of how to seamlessly integrate kdb+ into your organization, leveraging a modern tech stack including the Python ecosystem.

**Thanks for reading!**
