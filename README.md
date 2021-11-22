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
        <li><a href="#installation">Installation< & Usage/a></li>
        <li><a href="#api">API/a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Applicaiton for regulation complaince regarding time worked and time spent driving. Backend RESTful service that gathers events and uses those events to generate compliance reports. Uses Python's built in sqlite3 for storage.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Pytest](https://docs.pytest.org/en/6.2.x/)

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

### API

`/event PUT` Add a new Event representing the end of a work state, a duration of Driving, Working, or Off Work
* Parameters:
  * `work_status : string` : One of `D` representing Driving, `W` representing Working, or `OFF` for Off Work
  * `time : int` : number of minutes worker spent in work state
* Return `json`: The created and persisted Event with the same fields as the parameters:
  * `work_status : string` : One of `D` representing Driving,`W` representing Working, or `OFF` for Off Work
  * `time : int` : number of minutes worker spent in work state

`/clock GET` Get two clocks, built using previously submitted events. If time Off Work reaches `10` hours, clocks are reset. First is Drive clock, Second is Work clock
* Parameters: None
* Return `json`: Two Clocks with the following properties:
  * `type : string` : One of `DRIVE_CLOCK` representing the Drive clock,`WORK_CLOCK` representing Work clock
  * `violation_status : string` : Regulation status of the clock. One of `OK` if clock is within regulation,`V` if clock is in violation
  * `time_value : int` : number of minutes worker has on this clock since last reset, for `DRIVE_CLOCK` only `D`-Driving time is counted, for `WORK_CLOCK` all three are summed(`D`, `W`-Non-driving Work, `OFF`-Time not worked [breaks less than 10 consecutive hours])

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
- [x] Update to sqlite for storage, g doesn't work
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
    - [x] APIs
- [ ] Improvements
    - [ ] ? Add MongoDB
        - [ ] Event Document
        - [ ] DB tests
            - [ ] DB fixtures
    - [ ] ? Design notes
    - [ ] ? Add Docker
    - [ ] ? Add small templates for reports
    - [ ] ? Swagger


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
