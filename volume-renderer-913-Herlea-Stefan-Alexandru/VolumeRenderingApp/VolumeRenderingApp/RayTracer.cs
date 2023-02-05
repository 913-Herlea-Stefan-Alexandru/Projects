using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace VolumeRendering
{
    class RayTracer
    {
        private Object3D object3d;

        public RayTracer(Object3D object3d)
        {
            this.object3d = object3d;
        }

        private double ImageToViewPlane(int n, int imgSize, double viewPlaneSize)
        {
            var u = n * viewPlaneSize / imgSize;
            u -= viewPlaneSize / 2;
            return u;
        }

        public void Render(Camera camera, int width, int height, string filename)
        {
            var background = new Color(0.0, 0.0, 0.0, 1.0);
            var image = new Image(width, height);
            var searchStep = 0.5;
            var maxDist = 1000.0;

            var rgba = new Color[]{
                new Color(0.0, 0.0, 0.0, 0.0),
                new Color(1.0, 1.0, 0.0, 0.5),
                new Color(1.0, 0.0, 1.0, 0.5),
                new Color(0.0, 1.0, 0.0, 0.5)
            };
            var colorMap = new Dictionary<int, int>
            {
                {0, 13},
                {1, 100},
                {2, 200},
                {3, 256} 
            };

            for (var i = 0; i < width; i++)
            {
                for (var j = 0; j < height; j++)
                {
                    Vector pixelPoint = camera.Position + camera.Direction * camera.ViewPlaneDistance
                        + camera.Up * ImageToViewPlane(j, height, camera.ViewPlaneHeight)
                        + (camera.Up ^ camera.Direction).Normalize() * ImageToViewPlane(i, width, camera.ViewPlaneWidth);

                    Line ray = new Line(camera.Position, pixelPoint);
                    Color pixelColor = new Color();
                    bool wasInside = false;

                    image.SetPixel(i, j, background);

                    for (var t = 0.0; t < maxDist; t += searchStep)
                    {
                        Vector position = ray.CoordinateToPosition(t);

                        if (object3d.isInside(position))
                        {
                            var elem = object3d.getValue(position);

                            wasInside = true;

                            Color currentColor = new Color();

                            if (elem / 255.0 >= 0.15)
                            {
                                // black and white
                                // currentColor = new Color(elem / 255.0, elem / 255.0, elem / 255.0, 0.5);

                                // color
                                foreach (var key in colorMap.Keys)
                                {
                                    if (elem <= colorMap[key])
                                    {
                                        currentColor = rgba[key] * (elem / 255.0);
                                        /*currentColor.Red = rgba[key].Red * (elem / 255.0);
                                        currentColor.Green = rgba[key].Green * (elem / 255.0);
                                        currentColor.Blue = rgba[key].Blue * (elem / 255.0);
                                        currentColor.Alpha = rgba[key].Alpha;*/
                                        break;
                                    }
                                }

                                // update the color and the opacity using the formula discussed in the course

                                // F1
                                /*pixelColor = pixelColor * pixelColor.Alpha + currentColor * (1 - pixelColor.Alpha);
                                pixelColor.Alpha += (1 - pixelColor.Alpha) * currentColor.Alpha;*/

                                // F2
                                pixelColor = new Color(
                                    pixelColor.Red * pixelColor.Alpha + currentColor.Red * (1 - pixelColor.Alpha),
                                    pixelColor.Green * pixelColor.Alpha + currentColor.Green * (1 - pixelColor.Alpha),
                                    pixelColor.Blue * pixelColor.Alpha + currentColor.Blue * (1 - pixelColor.Alpha),
                                    pixelColor.Alpha + (1 - pixelColor.Alpha) * currentColor.Alpha
                                );

                                // F3
                                /*pixelColor += currentColor * (1 - alpha);
                                alpha += currentColor.Alpha * (1 - alpha);*/

                                image.SetPixel(i, j, pixelColor);

                                // if the opacity is >= 1 -> there is no need to continue, we can stop
                                if (pixelColor.Alpha >= 1)
                                {
                                    break;
                                }
                            }
                        }
                        else
                        {
                            if (wasInside)
                            {
                                break;
                            }
                        }
                    }

                    image.SetPixel(i, j, pixelColor);
                }
            }

            image.Store(filename);
        }
    }
}