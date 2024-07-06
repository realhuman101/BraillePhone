# <div align="center">Braille Phone</div>

<div align="center"><i>Our innovative Braille smartphone transforms text into touch, fostering inclusivity and independence for the visually impaired in the digital world.</i></div>

***

## Table of Contents

- [Braille Phone](#braille-phone)
	- [Table of Contents](#table-of-contents)
	- [Introduction](#introduction)
	- [Requirements](#requirements)
	- [Installation](#installation)
		- [Requirement Installation](#requirement-installation)
		- [Project Installation](#project-installation)
	- [Usage](#usage)
	- [Contributing](#contributing)
	- [License](#license)
	- [Credits](#credits)

## Introduction

> Please note that this project is simply a **prototype**.

Our project aims to assist the blind by providing them access to modern-day technology in the form of a smart phone. Through use of low-cost equipment, we can create an innovative and intuitive device accessible through use of braille to give the blind the same privileges as the average seeing person. This would not only include features like tactile buttons allowing users to interact with the device, but also allow the user to visualise text through use of pins to represent braille.

The scope of our project extends to the wider community for anyone who is visually impaired and is unable to access the benefits of a common smartphone. The Braille smartphone implements the Braille language to create a model of the smartphone which can be used by blind or partially blind members of our community. Hence, anyone who lacks the visual ability to use the smartphone and is relying on Braille to communicate is a key stakeholder and part of our clientele.

> Please also note that this is still a ***work in progress*** and is not yet complete.

## Requirements

- A Raspberry Pi (CAD models are designed for the Raspberry Pi 4)
- An Arduino UNO
- 3x Servos *(We used the `SG51R`)*
- Ability to 3D print components to hold parts together ***Preferable, not necessarily required***

## Installation

### Requirement Installation

Make sure to install Python3 and pip3 on your Raspberry Pi.

To install the required Python packages, run the following command **on the Raspberry Pi**:

```shell
pip install -r requirements.txt
```

Or, depending on your installation:

```shell
pip3 install -r requirements.txt
```

### Project Installation

To install the project, either `git clone` the repository or download the ZIP file with the green `code` button above.

## Usage

To use the project, you can:

1. Upload the [arduino.ino](assets/arduino/arduino.ino) file to your Arduino UNO
2. On the Raspberry Pi, connect to the internet
3. Wire up the servos to the Arduino UNO
4. Connect the Arduino UNO to the Raspberry Pi
5. Connect the buttons to the Raspberry Pi
6. On the Raspberry Pi, run the `main.py` Python script
7. Place the Raspberry Pi, Arduino UNO and the Servos into their respective areas on the 3D printed casing
8. Use the Braille Phone!

## Contributing

If you want to contribute to this project, please follow the guidelines below:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push the new branch to your fork
5. Submit a pull request

## License

This project is licensed under the MIT license. See our [LICENSE](LICENSE) for more information.

## Credits

- [Valentina Banner](https://github.com/realhuman101) - *Co-creator*
- [Maya Yan](https://github.com/mayahkg) - *Co-creator*
