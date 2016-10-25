# MapRoulette API Wrapper

## Project

### Create

_Only Superusers can create new Projects on the server._

```
s = Server()
p = Project()
p.name = "New Project"
p.post(s)
```

### Retrieve

```
s = Server()
p = Project(id)
p.retrieve(s)
```

### Modify

```
s = Server()
p = Project(id)
p.get(s)
p.name = "Modified Name"
p.put(s)
```

### Delete

_Only Superusers can delete Projects on the server._

```
s = Server()
p = Project(id)
p.delete(s)
```

## Challenge

### Create

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

### Retrieve

```
s = Server()
c = Challenge(id)
c.retrieve(s)
```

### Modify

```
s = Server()
c = Challenge(id)
c.get(s)
c.name = "Modified Name"
c.put(s)
```

### Delete

_This will also delete all child tasks!_

```
s = Server()
c = Challenge(id)
c.delete(s)
```

## Task

### Create

```
s = Server()
c = Challenge(id)
c.get(s)
t = Task()
t.location = 
```

### Retrieve

```
s = Server()
c = Challenge()
c.retrieve(s, id)
```

### Modify

```
s = Server()
c = Challenge()
c.get(s, id)
c.name = "Modified Name"
c.put(s)
```

### Delete

_This will also delete all child tasks!_

```
s = Server()
c = Challenge()
c.delete(s, id)
```

