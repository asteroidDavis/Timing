# Timing
A matlab function for creating a struct representing many desired timing elements of a 1D signal

# EXAMPLE
<pre>
timing = Timing(512, 256); 
% generate a wave 
wave = sin(2*pi*timing.t);
</pre>

#  Usage
There's only 1 function
See the function header

# Advice
Add elements which you need and remove elements you do not need

# Rewrite with OpenAPI
We're going to use the timing api which 
we originally implemented using Matlab.
Except we're going to implement it 
as a python and REST interface over 
a timeseries database.

Clients could add support for different tool
and material relations. We could also just work on a graphical client


REST/asteroidDavis-timing-1.0-swagger.yaml is the interface I'll be using.
- timing.py is responsible for the in memory representation and essentially copies the original timing.m
- timing.sql or similar will be responsible for persisting the objects in timing.py

- chalice, CDK, another aws tool should be used to set this up in my account with a lambda
- app.py is the routes for the app
- authentication/authorization can be handled with access tokens


