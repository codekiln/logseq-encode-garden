alias:: [[AWS ECS Predictive Scaling]]

- # AWS ECS Predictive Scaling
	- ML-based predictive scaling learns historical [[AWS/ECS]] service traffic, forecasts future load, and proactively adjusts task count + underlying [[AWS/EC2]] / [[AWS/Fargate]] capacity ahead of demand, boosting availability and cutting over-provisioning without manual schedules.
		- [Optimize compute resources on Amazon ECS with Predictive Scaling | Containers](https://aws.amazon.com/blogs/containers/optimize-compute-resources-on-amazon-ecs-with-predictive-scaling/?utm_source=chatgpt.com)
		- [Use historical patterns to scale Amazon ECS services with predictive scaling - Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-auto-scaling.html)
		- [Amazon Web Services, Inc.](https://aws.amazon.com/about-aws/whats-new/2024/11/predictive-scaling-for-amazon-ecs-services/?utm_source=chatgpt.com)
	- Attach a predictive scaling policy via Application Auto Scaling, review console forecasts, and optionally tune with custom or [[AWS/SQS]]-style metrics for precise control.
		- [Evaluate your predictive scaling policies for Amazon ECS - Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-graphs.html)
		- [Advanced predictive scaling policy using custom metrics for Amazon ECS - Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-custom-metrics.html)