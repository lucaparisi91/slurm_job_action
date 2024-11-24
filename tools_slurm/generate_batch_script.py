import argparse

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



default_job_config = {
        "job-name" : "runner_job",
        "time" : "0:20:0",
        "nodes": 1,
        "ntasks_per_node": 1,
        "partition": "standard",
        "qos": "short"
    }


def generate_batch_script(config):
    """
    Generates a batch script for slurm. 
    config: dict
    cmds: sequence of commands to execute on the compute node
    """

    batch_script=r"#!/bin/bash" + "\n"
    pre_directive="#SBATCH"

    for key,value in config.items():
        
        if key!="script":

            default_directive=key.replace("_","-")

            batch_script+=f"{pre_directive} --{default_directive}={value}\n"
        
    batch_script+=config["script"]

    
    
    return batch_script

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('config' , type=str, help="Yaml configuration file describing the job to run")
    

    script = ["pwd","hostname"]


    args= parser.parse_args()
    with open(args.config) as f:
        data=load(f,Loader=Loader)
    

    batch_script=generate_batch_script(data )

    print(batch_script)


