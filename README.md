AggregatedQC
---

## Two-step Workflow for Assessing NGS Read Quality and Aggregating the Quality Reports

AggregatedQC uses FASTQC to assess read quality for all availed read files in a directory, then employs MultiQC to aggregate the reports into one. It is an easy and quick to use workflow available freely on LatchBio.

## Input
- a directory with raw FastQ files i.e .fastq, .FASTQ, .fq or .FQ

## Output
- an aggregated QC report for all the files run.

## Quickstart
### Using AggregatedQC on LatchBio
1. Go to https://latch.bio, create an account or log in
2. Search for `AggregatedQC` via the `Explore` tab. See here https://console.latch.bio/explore/64831/info
3. Add `AggregatedQC` to your workspace
4. In the `Workflows` tab, click on `AggregatedQC`
5. Select a directory with the fastq files you want to assess or use the `Test data` within the workflow.
6. Then `Launch Workflow`  


## Links
- LatchBio: https://latch.bio
- Source code: https://github.com/RitahNabunje/aggregated_qc
