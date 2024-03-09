# maligner: An Open-Source Molecular Alignment Tool

![GitHub top language](https://img.shields.io/github/languages/top/hellmrf/maligner)
[![GitHub License](https://img.shields.io/github/license/hellmrf/maligner)](https://github.com/hellmrf/maligner/blob/main/LICENSE)
[![Powered by RDKit](https://img.shields.io/badge/Powered%20by-RDKit-3838ff.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAFVBMVEXc3NwUFP8UPP9kZP+MjP+0tP////9ZXZotAAAAAXRSTlMAQObYZgAAAAFiS0dEBmFmuH0AAAAHdElNRQfmAwsPGi+MyC9RAAAAQElEQVQI12NgQABGQUEBMENISUkRLKBsbGwEEhIyBgJFsICLC0iIUdnExcUZwnANQWfApKCK4doRBsKtQFgKAQC5Ww1JEHSEkAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMi0wMy0xMVQxNToyNjo0NyswMDowMDzr2J4AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjItMDMtMTFUMTU6MjY6NDcrMDA6MDBNtmAiAAAAAElFTkSuQmCC)](https://www.rdkit.org/)

## Installation

You shall have Python (preferably 3.11) installed. To install the package and dependencies, go to the repository's root folder and run:

```
python -m pip install . .[dev]
```

You can ommit `.[dev]` if you'll not work directly on the development

## Development

### Stage of development

The current stage of this project is: `IDEA`, so it's absolutely not ready for real usage. Your contribution would be very appreciated.

### Code formatting

We're using Google's [`yapf`](https://github.com/google/yapf) autoformatter together with `google` style-guide. You can install `yapf` on VSCode from the extensions marketplace. At command-line, it would be `yapf file.py`. Make sure you have it configured, so we don't conflict styling.

### Current plan

Currently, the plan for the UX of the software is the following.

**Main screen**:
- [X] The user can load molecules (in .mol, .mol2 or ??)
- [X] Can see a grid with all molecules and the filename
- [X] Can mark one molecule as anchor
- [X] Can go to structure selector.
- [ ] Options menu
- [ ] "Preview Alignment" and "Save Alignment" buttons.

**Options menu**
- Save action:
  - Overwrite original files
  - Suffix aligned files (option to write the suffix)
  - *(Default)* Save in a separate directory (default: `aligned`)

**Atom selector**:
- [X] User see the molecule and, by default, the MCS calculated.
- [ ] Three selection buttons: Select MCS, Select All, Select None.
- [ ] Two more buttons: Cancel, Save.
- [X] User can click on atoms to select/deselect.
- [ ] Select structure by SMILES/SMARTS.
- [ ] Maybe implement lasso tool in future.

At this stage, users can load molecules, anchor one of them, and they are displayed in a grid view. The user can automatically select MCS on all molecules. The user can click twice on a molecule and it will take it to Substructure Selector, where the selected atoms can be tweaked by clicking. Now we need to implement the alignment part. I have some drafts already.