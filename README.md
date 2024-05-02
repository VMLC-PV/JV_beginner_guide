# Beginner’s guide to visual analysis of perovskite and organic solar cell current density-voltage characteristics
Drift-diffusion simulations in support of the 'Beginner’s guide to visual analysis of perovskite and organic solar cell current density-voltage characteristics', as published in Advanced Energy Materials: https://doi.org/10.1002/aenm.202400055

## Description
This repository includes the code utilized in the research paper titled "Beginner’s guide to visual analysis of perovskite and organic solar cell current density-voltage characteristics." Here, you'll find resources to replicate all simulations featured in the academic publication.

The publication introduces an easy-to-follow flowchart to analyze organic and perovskite solar cells mainly based on light intensity-dependent current density-voltage characteristics measurements. Each endpoint (green rectangle) of this flowchart indicates the dominant loss mechanism of your solar cell and is accompanied by a drift-diffusion simulation that can be reproduced with the code in this repository.

The flowchart is depicted below:

![Flowchart to determine the main losses of an organic or perovskite solar cell](Flowchart.jpg)

## Overview
The repository contains four Jupyter notebooks—'Beginners_guide_OPV.ipynb', 'Beginners_guide_Pero.ipynb', 'OPV_Exp_Simu.ipynb', and 'Perov_Exp_Simu.ipynb'—which serve as the backbone for running these simulations. These notebooks can be used to reproduce all analyses presented in the research paper. Additionally, they are intuitive to use, so you can adjust all parameters and re-run the simulations with your values. The notebooks can be used to run the simulations and plot the data. They can be run on Windows and Linux. However, running simulations in parallel is not possible on Windows, yet.

## Simulations Tools

The simulations are executed using the open-source software Simsalabim written by Prof. L. Jan Anton Koster from the University of Groningen. (See [GitHub repository](https://github.com/kostergroup/SIMsalabim))

## Installation

Clone the repository and install the requirements needed. The requirements can be installed with the following command:

```
pip install -r requirements.txt
```
To compile Simsalabim, please follow the instructions in the Simsalabim [GitHub repository](https://github.com/kostergroup/SIMsalabim).

## Contribution and Collaboration
Contributions, issues, and pull requests are welcome, fostering collaboration and further development within the scope of this research. Feel free to explore, utilize, and adapt the codebase to extend the knowledge and potential applications of these simulations.

We hope this repository serves as a valuable resource for anyone interested in understanding, replicating, and furthering the analysis of perovskite and organic solar cell characteristics.

Thank you for your interest and exploration!
