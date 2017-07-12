## NASA ROBOT Challenger

Technical Challenger

## Objectives

* The terrain should be 5x5 dimension.
* The robot starts in the position (0,0,N).
* The rebot returns the final position after execute command.
* The robot should respect the terrain limits.
* The robot should't save positions log.

## Request API example

Command:

`curl -s --request POST http://localhost:8080/rest/mars/MMRMMRMM`

Response:

```
{ "x": 2, "y": 0, "d": "S" }
```

* "x" to axis x
* "y" to axis y
* "d" to direction ("W"est, "N"orth, "E"ast and "S"outh)

## Docker runner

### Start

`./run_container.sh start`

### Stop

`./run_container.sh stop`

### Unit tests

`./run_container.sh tests`

## Standalone execution

### Prerequisites to API

`pip3 install eve`

### Start API

`python3 run.py`

## Tests

### Prerequisites to tests

`pip3 install requests unittest`

### Unit tests

`puthon3 tests.py`
