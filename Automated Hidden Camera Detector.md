# Automated Hidden Camera Detector

## Project Description

This project is used for GeekPwn 2019 Anti Sneak Shot Challenge. This project is a device that makes it easy to find hidden cameras that may be in your room. It can finish most of the work by itself automatically. 

## Project Principle Introduction

Base on research, we find out that we can use the following methods to find hidden cameras:

- Most of the camera has a "clock" that can control the image sensor to shoot each pixels, and this will emit radio waves into the air. If we can pick up the radio wave in the air and judging frequency to make sure it comes from a camera but not other devices. After that, if we can find out where is the radio wave from, we can find the position of the hidden cameras.

- Every camra will heat up during recoding, so if we use infrared thermal imaging sensor to find out the hotest place in the room, we can figure out where is the hidden cameras. But this method cannot distinguish the cameras and other electric devices. And in this challenge, all the stuff is cover by cloth, so this may not be a good solution.

- Most of the camera have metal inside, so we can use metal detector to search the metal in the room. Maybe we cannot figure out the precise position but at least we can know how many cameras is in the room. The biggest advantage of this solution is it can detected the cameras which is not turned on, but it also brings some trouble at the same time <!-- but at the same time it also brings some trouble  --> - many chairs or desks are made from metal as well<!--,-->. So we need to find out the different between a hidden camera and other metal things. Maybe we can use machine learning to help us with this solution.



## Specific Implementation Plan

## Usage Instructions

## Project Prospects & Similar Products Comparison

## References
