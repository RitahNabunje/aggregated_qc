"""
Assess NGS read quality with FastQC and aggregate quality reports with MultiQC.
"""

import subprocess
from pathlib import Path
import multiqc
from latch import small_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def qc_assessment(input_dir: LatchDir) -> LatchDir:
    """
    Run fastqc on all read files in the input directory.
    """
    q_files = ['.fastq', '.fq', '.FASTQ', '.FQ']
    input_files = [f for f in Path(input_dir).iterdir() if f.suffix in q_files]
    # output directory
    output_dir = Path("aggregated_qc")
    # make output_dir
    _outdir_cmd = [
        "mkdir",
        "aggregated_qc"
    ]
    subprocess.run(_outdir_cmd)

    _fastqc_cmd = [
        "fastqc",
        "--o",
        str(output_dir),
        *input_files
    ]

    subprocess.run(_fastqc_cmd)

    return LatchDir(str(output_dir), f"latch:///{output_dir}")


@small_task
def aggregate_reports(reports_dir: LatchDir) -> LatchDir:
    """
    Run Multiqc on all qc report files in the input directory.
    """
    # output file
    out_dir = f"aggregated_qc"
    out_file = f"{out_dir}/aggregated_qc_report.html"

    _multiqc_cmd = [
        "multiqc",
        reports_dir,
        "-n",
        out_file
    ]
    subprocess.run(_multiqc_cmd)

    return LatchDir(str(out_dir), f"latch:///{out_dir}")


@workflow
def aggregated_qc(input_dir: LatchDir) -> LatchDir:
    """Description...

    Read Quality Assessment with FastQC and QC Report Aggregation with MultiQC
    ----

    FastQC performs quality control checks on
    raw sequence data from high throughput
    sequencing.

    MultiQC aggregates results from the
    analyses across many samples into a single
    report.

    __metadata__:
        display_name: AggregatedQC
        author:
            name: Ritah Nabunje
            email: ritahnabunje@gmail.com
            github: https://github.com/RitahNabunje
        repository: https://github.com/RitahNabunje/aggregated_qc
        license:
            id: MIT

    Args:

        input_dir:
          Paired-end or single-end fastq read files to be assessed.

          __metadata__:
            display_name: Input Directory

    """
    return aggregate_reports(reports_dir=qc_assessment(input_dir=input_dir))
