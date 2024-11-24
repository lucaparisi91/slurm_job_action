# slurm_job_action

A custom action to submit a job to a slurm cluster.
Currently this is only a rough implementation for Archer2.
You can find an exemple on how to use this action below.

```yaml
submit_parallel_job:
      name: submit_parallel_job
      # needs: setup
      runs-on: self-hosted
      steps:
        - name: Show hostname
          uses: lucaparisi91/slurm_job_action@v0.01
          with:
            job-name: "runner_job"
            time: "0:20:00"
            nodes: 1
            ntasks_per_node: 1
            partition: standard
            qos: short
            script: |
              hostname
              sleep 30
```