# Dream Lab Walk-through

A 3D, walk-around model of a dream robotics lab in a Hobart warehouse: a loft living area, a car bay, a gym, a skatepark and a rooftop deck. It is one self-contained HTML file (`index.html`) built with [three.js](https://threejs.org/) r128, which loads from the cdnjs CDN.

**Live page:** https://lijeythefox.github.io/Random-Claude-Code-Stuff/dream-lab-3d/

## How to run it

- **Online:** open the live page link above.
- **On your own computer:** download `index.html` and double-click it to open it in Chrome, Edge or Firefox. It needs an internet connection the first time, so it can load three.js.

## Controls

| Action | Keyboard / mouse | Touch |
|---|---|---|
| Look around | Click the view, then move the mouse | Drag on the view |
| Walk | `W` `A` `S` `D` or the arrow keys | Joystick, bottom left |
| Run | Hold `Shift` | — |
| Ride the slide / climb to the roof / go back down | `E`, or the button that appears | The button that appears |
| Turn labels on or off | `L`, or the **Labels** button | **Labels** button |
| Day / night | `N`, or the **Night mode** button | **Night mode** button |
| Free the mouse | `Esc` | — |
| Jump to an area | The quick-travel buttons along the bottom | Same |

## What's in it

- **Ground floor:** electronics and assembly benches, a debugging area, a parts library, a skatepark, a fab shop, a PCB line, a server room, a recording studio, a film stage, a netted robot test arena, a car display bay, a gym with a cedar sauna, a bouldering wall and a downstairs bathroom.
- **Loft:** bedrooms, a bathroom, battlestations, a fireside chat corner, a lounge with a TV, LEGO shelf, jukebox and CD wall, a kitchen and dining area, a drinks and snack fridge, and a games corner with arcade machines, pinball, foosball and the slide.
- **Rooftop:** reached by the spiral stairs at the kitchen end of the loft. It has a deck with outdoor sofas, a fire table, string lights, a BBQ and a telescope, plus a solar array and a view of hills, a river and the city.
- **Extras:** a lab cat that wanders, sits and naps; neon signs; and day/night lighting.

The movie posters, arcade game names, artwork and skate deck designs are original, made for this model.

## Editing it

Everything is in `index.html`. The scene is built in plain JavaScript using small helper functions:

- `B` makes boxes, `Cy` cylinders and `Sp` spheres.
- `O` makes a group at a given x/z position.
- `col` and `fp` add walls you can't walk through.
- `label` adds a floating name tag.

Quick-travel spots are in the `SPOTS` list, and minimap zones are in `ZN`. After editing, open the file in a browser to check it.
