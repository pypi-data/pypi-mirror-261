# Flow Tuning

## Setup

It's recommended to use DevContainers. Otherwise, you should install the following:

- Python 3.12
- Poetry

You could try the example by executing the following commands:

```bash
mkdir -p tmp
cp examples/01-function-tuning.yml tmp/function-tuning.yml
poetry run ft function -c ./tmp/function-tuning.yml
```

## Commands

Use `poetry run ft --help` to see the available commands.

## Directory Structure

```
- benchmarks     # Benchmarks to test algorithms (WIP)
  |- function    # Function benchmarks
  -- workflow    # Workflow benchmarks
- examples       # Config examples
- flow_tuning    # Source Code
  |- algorithms  # Tuning algorithms
  |- generators  # Function payload generators
  |- providers   # Cloud platform providers
  |- utils       # Utilities
  -- cli.py, function.py, workflow.py
                 # Cli and command routines
```

## Supported algorithms

| Algorithm   | Description                                                                                               | Function | Workflow |
| ----------- | --------------------------------------------------------------------------------------------------------- | -------- | -------- |
| PowerTuning | A modified version of [AWS Lambda Power Tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning) | ✅       | ❎       |
| OrionTurbo  | Simplified [Orion OSDI'22](https://www.usenix.org/conference/osdi22/presentation/mahgoub)                 | ❎       | ✅       |
