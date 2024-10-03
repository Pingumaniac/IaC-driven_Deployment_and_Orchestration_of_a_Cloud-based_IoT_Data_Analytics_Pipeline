# CS5287_Cloud_Computing_Team6_Homework2
IaC-driven Deployment and Orchestration of a Cloud-based IoT Data Analytics Pipeline using Virtual Machines and Docker

## Goals - Key changes from PA1

Instead of the manual approach in PA1, PA2 will automate the process using Infrastructure-as-Code (IaC) frameworks, in our case Ansible.

1.	Ansible playbooks: Convert all the manual steps that you have documented in PA1 into Ansible plays. This will involve creating the four VMs, installing all the necessary packages (including Docker for this assignment), setting firewall rules, downloading and installing Kafka distribution all accomplished using Ansible plays. A skeleton master playbook has been provided. You will have to fill up the logic for all the child playbooks that are invoked by the master playbook. Make changes as deemed necessary.
2.	Producer code changes: Since our producer is currently sending traffic in one-way direction as it behaves as a strict publisher, we will need to enhance the producer code such that it runs an additional thread that behaves as a consumer. We need this capability to collect the end-to-end response times for ML inferencing for every sample that we send in the pipeline.  The producer’s consumer thread will now read the “inference result” topic from the Kafka broker but only the sample that corresponds to the original image sent by this producer. The reason we need to match this is because we are going to run multiple producers as described below. Recall that the ML inference server already produces this topic to the Kafka broker for every sample it is inferencing, and you are already updating the database with the result.
3.	Execution of the data pipeline: Manually execute Kafka, ZooKeeper and DB as processes just like we did in PA1 on VMs distributing them evenly across the VMs. However, we will execute the producer, consumer and ML server inside Docker containers. Distributed these containers also across the four VMs. Let the producer send at least 1,000 samples at some frequency like one sample per second. Collect all the end-to-end latency results and save them to a file for later graph plotting.
4.	Workload variation: Once you have the pipeline working, we now increase the workload by introducing multiple producers running in their own containers. We test our solution varying the number of producers from 1 to 4. Basically, we run one producer inside its container on each VM.

## Technologies Used
1. Python 3
2. Apache Kafka
3. MongoDB
4. Chameleon Cloud with Ubuntu Linux version 22.04 image (CC-Ubuntu22.04 on Chameleon)
5. CIFAR-10 image data set used by the IoT source.
6. Docker
7. Ansible

## Instructions for setting up the technologies used

1. Install the following Python packages through your chosen CLI.

```
pip3 install kafka-python
pip3 install torch torchvision
pip3 install pymongo
```

2. Install Docker Image for Apache Kafka.

```
docker pull apache/kafka
```

3. Download Apache Kafka on your chosen directory using wget or curl -0 command.

```
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
```

```
curl -O https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
```

Then, unzip the file, and move to the kafka directory.

```
tar -xzf kafka_2.13-3.8.0.tgz
cd kafka_2.13-3.8.0
```

## How work was split

* Robert Sheng primarily worked on...
* Youngjae Moon primarily worked on...
* Lisa Liu primarily worked on...

## Team Members

* Young-jae Moon (MS, youngjae.moon@vanderbilt.edu
* Robert Sheng (BS/MS, robert.sheng@vanderbilt.edu
* Lisa Liu (BS, chuci.liu@vanderbilt.edu

under Professor Aniruddha Gokhale, a.gokhale@vanderbilt.edu
