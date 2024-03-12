# Lucy SPC

Lucy SPC is a Python library ( name inspired by the character Lucy Pevensie from the Narnia movie series ) provides functionalities to read and write .spc (Special Configuration) files, allowing easy conversion to and from JSON format.

## Installation

You can install Lucy SPC via pip:

```bash
pip install lucy-spc
```

## Usage

### Reading .spc Files

```python
import lucy_spc as cf

# Initialize Config object with the path to the .spc file
spc = cf.Config("example.spc")

# Read the .spc file and convert it to JSON format
json_data = spc.readLucy()

# Print the JSON data
print(json_data)
```

### Modifying JSON Data

```python
# Modify the JSON data as needed
spc.jsonData["aws2"]["secret_key"] = "new_secret_key"

# Write the modified JSON data back to the .spc file
spc.writeLucy()
```

### Writing .spc Files

```python
# Create a new JSON object with the desired configuration
new_config = {
    "connection1": {
        "plugin": "aws",
        "secret_key": "my_secret_key",
        "access_key": "my_access_key",
        "regions": ["us-east-1", "us-west-2"]
    },
    "connection2": {
        "plugin": "gcp",
        "secret_key": "another_secret_key",
        "access_key": "another_access_key",
        "regions": ["us-central1", "us-west1"]
    }
}

# Initialize Config object with a new .spc file path
new_spc = cf.Config("new_config.spc")

# Assign the new JSON data
new_spc.jsonData = new_config

# Write the JSON data to a new .spc file
new_spc.writeLucy()
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This library was inspired by the character Lucy Pevensie from the Narnia movie series.
- Special thanks to myself.
