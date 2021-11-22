<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Applicaiton for regulation complaince regarding time worked and time spent driving. Backend RESTful service that gathers events and uses those events to generate compliance reports.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python]()
* [Flask]()
* [Pytest]()

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Needed before installation:
* python >3.8
* pip

Used and installed by package
* flask
* pytest

### Installation & Usage

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/compliance_clock.git
   ```
2. Move to package
   ```sh
   cd compliance_clock
   ```
3. Install editable package and dependencies
   ```sh
   python -m pip install -e compliance_clock
   ```
4. Set your FLASK_APP environment variable to `compliance_clock`
   ```sh
   export FLASK_APP=compliance_clock
   ```
4. Run flask
   ```sh
   python -m flask run
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Flask App
    - [x] App runs and is installable
- [x] Endpoints
    - [x] Event
    - [x] Summary
- [x] Basic Flask.g backed Models
    - [x] Event
    - [x] Single Shift Summary (no time off reset)
    - [x] Move storage to consisent layer
    - [x] Rename to match Requirements
    - [x] Add time off reset to Summary
- [ ] Update to something else for storage, g doesn't work
- [x] Service Runs
- [x] Tests and Coverage
    - [x] Basic Tests for framework
    - [x] Summary Tests 
    - [x] Unit test examples from Requirements 
    - [x] Flask fixtures
    - [x] Endpoint tests
    - [x] App test
        - [x] Full test examples from Requirements
- [ ] Documentation
    - [x] GitHub
        - [x] Repository and README
        - [x] Roadmap/TODO
        - [x] Summary
        - [x] Instructions
    - [ ] APIs
        - [ ] Swagger?
    - [ ] General Code documentation
- [ ] Improvements
    - [ ] ? Design notes
    - [ ] ? Add MongoDB
        - [ ] Event Document
        - [ ] DB tests
            - [ ] DB fixtures
    - [ ] ? Add Docker
    - [ ] ? Add small templates for reports


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
