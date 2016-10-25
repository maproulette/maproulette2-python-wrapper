# MapRoulette API Wrapper

## Install

_PyPi to follow..._

On your local machine:

```
./setup.py install
```

## API

### Project

#### Create

_Only Superusers can create new Projects on the server._

```
s = Server()
p = Project()
p.name = "New Project"
p.post(s)
```

#### Retrieve

```
s = Server()
p = Project(id)
p.retrieve(s)
```

#### Modify

```
s = Server()
p = Project(id)
p.get(s)
p.name = "Modified Name"
p.put(s)
```

#### Delete

_Only Superusers can delete Projects on the server._

```
s = Server()
p = Project(id)
p.delete(s)
```

### Challenge

#### Create

Each Challenge needs a valid parent Project

```
s = Server()
p = Project(id)
p.get(s)
c = Challenge(id)
c.name = "New Challenge"
c.parent = p
c.post(s)
```

#### Retrieve

```
s = Server()
c = Challenge(id)
c.retrieve(s)
```

#### Modify

```
s = Server()
c = Challenge(id)
c.get(s)
c.name = "Modified Name"
c.put(s)
```

#### Delete

_This will also delete all child tasks!_

```
s = Server()
c = Challenge(id)
c.delete(s)
```

### Task

#### Create

```
s = Server()
c = Challenge(id)
c.get(s)
t = Task()
t.instruction = "Solve this please"
t.parent = c
t.location = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Point",
        "coordinates": [
          -98.4375,
          39.095962936305476
        ]
      }
    }
  ]
}
t.post(s)
```

#### Retrieve

```
s = Server()
t = Task(id)
t.retrieve(s)
```

#### Modify

```
s = Server()
t = Task(id)
t.get(s)
t.instruction = "Modified Instruction"
t.put(s)
```

#### Delete

```
s = Server()
t = Task(id)
t.delete(s)
```

## Run Tests

```
export MR_API_KEY=your_api_key && ./test_maproulette2.py
```
