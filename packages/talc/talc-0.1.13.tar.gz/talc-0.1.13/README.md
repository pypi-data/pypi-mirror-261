## What Talc Does

LLM applications often require custom datasets to develop and improve outputs. This is relevant not only during the training and tuning process of creating a model, but also during the software development cycle for feedback and testing on new changes.

Historically this has been done with human labelers, but humans are slow and often incorrect.

Talc provides the tooling to generate custom synthetic data that matches your specifications, and use those datasets to reliably test your AI.

## Quick Start
### Install & Setup
Most interactions with Talc can be managed with the Talc command line tool, which you can install with:

```bash
pip install talc
```

Your onboarding partner will provide you with an API key to access the Talc service, which can be set via the TALC_API_KEY environment variable like so

```bash
export TALC_API_KEY=<YOUR_API_KEY_HERE>
```

### Generating test sets

Talc generates test sets using a knowledge base provided by the user. The knowledge base can be generated from one or more documents or web pages. Supported file types include .txt, .pdf, .md, and .html.

The simplest way to get started with Talc is to generate a test set based on a folder containing your knowledge base files:

```bash
talc generate --dataset_name <name> --file <path_to_kb> --out <output_file.csv>
```

This process will generate a set of test questions across the provided directory. The resulting questions are saved to Talc, and downloaded in the form of a CSV file that can be used to evaluate your service.

The Talc API provides additional features such as providing sample data, grading rubrics, configuring for known failure modes and more.

For a full set of arguments to the generate command, use the `--help` flag:

```bash
talc generate --help
```

### Running tests

Tests are provided in the form of a CSV file (when using the CLI) or JSON (when using the API). 

The key fields returned are as follows:

```
Id: string // unique identifier used for grading API
Question: string // text of the question
```

It’s up to you to run these test scenarios against your language model application. This can be done manually for small test batches, or using a test harness for more extensive or automated tests.

### Grading test results

The results of testing should be formatted in a CSV file with the following columns

```
Id: string // unique identifier of the question asked from above
Answer: string // output of your LLM application
```

Test results (in the form of a CSV file) can be evaluated using the eval API. Via command line, run:

```bash
talc eval --infile <answers.csv>
```

This command will grade the tests and print overall stats such as accuracy to the terminal. The command supports the --print_failed and --save_failed <filename> to export failed test cases for further analysis.

For a full set of arguments to the generate command, see the full documentation (WIP).

### Github Actions Integration

You can use the Talc CLI as part of a Github Action workflow or any other CI system -- you'll just need to support the step of testing the Talc scenarios against your application. For more on Github Actions, see docs.github.com/en/actions/quickstart

## Data Privacy

Talc AI is built by a team with significant privacy and security experience, and this has shaped how the product is built since day 1. We’re in the process of certifying our SOC 2 type II compliance and anticipate finalization by Q2 2024.

At a brief glance:
1. Your data is encrypted at rest with AES-256 and in transit via TLS.
1. Your data is shared with cloud providers (e.g, AWS) that we use for hosting, all of whom are SOC 2 type II compliant. The exact set of providers depends on the configuration of your instance of Talc, which we’ll discuss before implementation
1. You can see the full breakdown of how we use data in our privacy policy.