def end_pipe(func, item):
    '''Allows to compose void-functions as if they where written in a functional style 
    or to execute a side-effect before returning another function result.
    End_Pipe(shuffle, list(range(9)))
    proces(End_Pipe(dblogger, user.getrequest()))'''
    func(item)
    return item

def se_pipe(func, iterable):
    '''Side-Effect Iterator: Allows to execute a function without breaking the original 
    dataflow nor splitting the iteration logic in several lines.
    Useful when an iterator is already defined and you want to perform addittional work
    onto each item before continuing the iteration proces.
    Furthermore, the resulting iterator is still composable.'''
    for item in iterable:
        func(item)
        yield item

def swap_pipe(func, iterable, obj):
    '''Version of reductions() for objects with state mutation methods.
    Allows to write sequential constructive/destructive updates as an iterator
    that yields the intermediate states.
    This allows to perform additional operations related to the intermediate states
    without altering the object mutation logic.
    Warning: the intermediate states are references to the object being updated, if you mutate them 
    you're mutating the original object too, wich in turn may affect the iteration with weird results.'''
    for x in iterable:
        func(item)
        yield obj

def cond_map(patterns, iterable):
    '''Would be equivalent to map(lambda x: if pred1(x): f1(x) elif pred2(x): f2(x) ··· else predk(x): fk(x), seq)
    i.e.: A map with multiple predicates that lead to different transformation functions.
    It emulates some of the behaviour offered by clojure's condp function.'''
    for x in iterable:
        for pred, func in patterns:
            if pred(x):
                yield func(x)
                break

def key_split(pred, iterable):
    '''Similar to groupby() from itertools, but returns a dictionary containing the keys paired with the list of items. 
    The lists preserve partial order: Idx(vec[x]) < Idx(vec[y]) ==> Idx(ksplit[q][x]) < Idx(ksplit[q][y])'''
    bag = {}
    for x in iterable:
        key = pred(x)
        if key in bag:
            bag[key].append(x)
        else:
            bag[key] = [x]
    return bag

def dispatch_all(fname, objls, item):
    '''Updates a sequence of object instances calling a method on each of them.
    May substitute obj.func(item) in code that acts on unknown type instances.'''
    for obj in objls:
        getattr(obj, name)(item)
