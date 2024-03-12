from setuptools import setup, find_packages

setup(
    name='MFE_GaussF',
    version='0.1.2',
    packages=find_packages(),
    description='A sophisticated tool for normalizing and quantifying isoform counts from RNA-seq data',
    license='MIT',  # Adjust the license as per your LICENSE file
    author='Qiang Su',
    author_email='qiang_su@hotmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/QiangSu/MFEGaussF',
    install_requires=[
        # Add your dependencies here
        # e.g., 'numpy>=1.18.1',
    ],
    entry_points={
        'console_scripts': [
            'merge_normalized_isoform_count_TPM=MFE_GaussF.merge_normalized_isoform_count_TPM:main',
            'merge_normalize_isoform_count_v1=MFE_GaussF.merge_normalize_isoform_count_v1:main',
            'kmer_frequency_distribution_mini_shared=MFE_GaussF.mkmer_frequency_distribution_mini_shared:main',
            'kmer_counting_loop=MFE_GaussF.kmer_counting_loop:main',
            'pipeline_abundance_GaussF_esti_loop=MFE_GaussF.pipeline_abundance_GaussF_esti_loop:main',
            'MFE_GaussF_esti=MFE_GaussF.MFE_GaussF_esti:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Ensure this matches your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
