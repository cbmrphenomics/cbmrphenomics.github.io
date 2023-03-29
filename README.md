# CBMR Phenomics documentation

This repository contains sources for public documentation and files related to usage of the esrum Esrum cluster administrated by CBMR phenomics. The documentation can be read at [cbmrphenomics.github.io](https://cbmrphenomics.github.io).

## Writing documentation

Documentation in automatically deployed to `cbmrphenomics.github.io/`:

1. Files in the `root/` folder are deployed directly to the root of `cbmrphenomics.github.io/`.
2. The [sphinx](https://www.sphinx-doc.org/en/master/) project in the `esrum/` folder is deployed to `cbmrphenomics.github.io/esrum/`.

To add additional sources of documentation, modify `.github/workflows/default.yaml`.

## Tools for writing documentation

### Automatically rebuild documentation

The `sphinx-autobuild` command can be used to automatically rebuild the documentation when you make changes:

```console
pip install --user sphinx-autobuild
cd /path/to/cbmrphenomics.github.io/esrum
sphinx-autobuild ./source ./build -q
```

Then go to [127.0.0.1:8000](http://127.0.0.1:8000/). The page automatically refreshes when you save changes to the documentation.

### Automatically format RST files

The `rstfmt` command can be used to automatically format `.rst` files for consistency:

```console
cd /path/to/cbmrphenomics.github.io/esrum
find -name '*.rst' | rstfmt
```

If using VSCode, the [Custom Local Formatters](https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters) extension can be used to enable automatic formatting of documentation. This requires merging the following configuration into your workspace configuration:

```json
{
  "customLocalFormatters.formatters": [
    {
      "command": "/path/to/rstfmt",
      "languages": [
        "restructuredtext"
      ]
    }
  ],
  "editor.formatOnSave": true
}
```
