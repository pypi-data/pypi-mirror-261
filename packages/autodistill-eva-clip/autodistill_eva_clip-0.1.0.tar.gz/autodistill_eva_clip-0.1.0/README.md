# Autodistill EvaCLIP Module

This repository contains the code supporting the CLIP base model for use with [Autodistill](https://github.com/autodistill/autodistill).

[EvaCLIP](https://github.com/baaivision/EVA/tree/master/EVA-CLIP),  is a computer vision model trained using pairs of images and text. It can be used for classification of images.

Read the full [Autodistill documentation](https://autodistill.github.io/autodistill/).

Read the [EvaCLIP Autodistill documentation](https://autodistill.github.io/autodistill/base_models/evaclip/).

## Installation

To use EvaCLIP with autodistill, you need to install the following dependency:


```bash
pip3 install autodistill-evaclip
```

## Quickstart

```python
from autodistill_evaclip import EvaCLIP
from autodistill.detection import CaptionOntology

# define an ontology to map class names to our EvaCLIP prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = EvaCLIP(
    ontology=CaptionOntology(
        {
            "person": "person",
            "a forklift": "forklift"
        }
    )
)

results = base_model.predict("./context_images/test.jpg")

print(results)

base_model.label("./context_images", extension=".jpeg")
```
## License

The code in this repository is licensed under an [MIT license](LICENSE.md).

## 🏆 Contributing

We love your input! Please see the core Autodistill [contributing guide](https://github.com/autodistill/autodistill/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!
