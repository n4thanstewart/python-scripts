# Lunar Lander

This is my solution to the common Python coding homework task.

For a breakdown and **explanation** of the code [see this document](https://docs.google.com/document/d/1RJafO-U9N3CYPYn95k077ejFx8q94OU7rcAe7nNx8uI/edit?usp=sharing).

## Notes:
To play the game, run the script in a Python IDE.

The height is set to 600m and the fuel __only 35s__ instead of 90, which makes the game only last around a minute with an optimal amount of fuel to use. Change these at the top of the script to customise the game.

## Objective
Computer simulation is used by engineers to test out ideas before actually building
expensive machines or putting people in dangerous situations.
Simulation is a critical part of the the space program by NASA, for example.

For this program, you will create a simulation of a vehicle landing on the moon. (It turns out
that this task is also a rather old computer game.)

Here is how it works: You are in control of a lunar lander ship, descending to the surface of the moon for a landing. Gravity steadily accelerates your ship toward the surface of the moon. You, the commander piloting the ship, have a single control: a button with the label "Burn". Applying thrust slows your ship down. Your goal is to get your ship to land on the moon at a slow enough speed (<10m/s) so that it doesn't crash on impact.

Your mission: Program this simulation in Python.

* a (for the moon) = -1.625 m/s^2
* a (for the rockets) = 2.5 m/s^2

Therefore: acceleration with the motors on = 0.875 m/s^2

*newheight = initialheight + 1/2at^2 + vt*

*newvelocity = v + at*

Where

* v = initial velocity
* t = time (either due to a burn or gravity)

## Additional work
You have only a limited amount of fuel (90s). If you slow down your ship too much too
early, you will run out of fuel and crash into the surface of the moon.