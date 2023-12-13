:orphan:

.. _p_tips_batching:

#################################
 Batching commands outside Slurm
#################################

***************************************
 Running commands sequentially in bash
***************************************

If you need to run a number of (very) short running commands, then it is
likely more efficient to do so with a simple loop in your ``sbatch``
script. For example, this script runs the ``plonk`` command on a number
of population VCF files:

.. code:: bash

   #!/bin/bash
   module load plonk/3.14
   for pop in CHB FIN GBR JPT PUR YRI; do
     plonk --input "./my_data/${pop}.vcf" --output "./my_results/${pop}.out"
   done

The following command indexes a number of (small) BAM files in the
current directory:

.. code:: bash

   #!/bin/bash
   module load samtools/1.17
   for filename in ./*.bam; do
     samtools index ${filename}
   done

However, it is important to remember that the total runtime will be the
*sum* of run-times for each task, since they are run one after the
other. It is therefore not recommended to use loops like this for
commands that take more than a few of minutes to complete!

**************************************
 Running commands in parallel in bash
**************************************

.. code:: bash

   module load plonk/3.14
   module load parallel/20230822
   parallel -P ${SLURM_CPUS_PER_TASK} \
     plonk --input "./my_data/{}.vcf" --output "./my_results/{}.out" \
     ::: CHB FIN GBR JPT PUR YRI
