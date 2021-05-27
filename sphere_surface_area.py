#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program calculates the surface area of a sphere

import math


def sphere_surface(radius):
    # This program calculates the surface area of a sphere

    # process
    surface_area = math.pi * 4 * (radius * radius)

    return surface_area


def main():
    # this function receives input
    print("This program calculates the surface area of a sphere.")
    print("")

    # input
    while True:
        try:
            radius_input = input("Enter the radius of the sphere (cm): ")
            radius_int = int(radius_input)
            print("")

            if radius_int > 0:
                # call function
                sphere = sphere_surface(radius_int)

                surface_rounded = '{0:.4g}'.format(sphere)

                print("Your sphere with the radius of {0} cm has a surface"
                      " area of {1} cm²."
                      .format(radius_int, surface_rounded))

                break
            else:
                # output
                print("Please input a positive integer. Try again.")
                print("")
        except Exception:
            # output
            print("{0} is not a number! Please try again.".format(radius_input))


if __name__ == "__main__":
    main()
