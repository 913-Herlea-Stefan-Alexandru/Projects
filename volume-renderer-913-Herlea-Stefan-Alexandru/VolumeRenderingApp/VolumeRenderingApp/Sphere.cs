using System;

namespace VolumeRendering
{
    public class Sphere : Geometry
    {
        private Vector Center { get; set; }
        private double Radius { get; set; }

        public Sphere(Vector center, double radius, Material material, Color color) : base(material, color)
        {
            Center = center;
            Radius = radius;
        }

        public override Intersection GetIntersection(Line line, double minDist, double maxDist)
        {
            double xc = Center.X;
            double yc = Center.Y;
            double zc = Center.Z;

            double b = line.X0.X;
            double d = line.X0.Y;
            double f = line.X0.Z;
            double a = line.Dx.X;
            double c = line.Dx.Y;
            double e = line.Dx.Z;

            double A = Math.Pow(a, 2) + Math.Pow(c, 2) + Math.Pow(e, 2);
            double B = 2.0 * (a * b - a * xc + c * d - yc * c + e * f - e * zc);
            double C = Math.Pow((b - xc), 2) + Math.Pow((d - yc), 2) + Math.Pow((f - zc), 2) - Math.Pow(Radius, 2);

            double delta = Math.Pow(B, 2) - 4 * A * C;
            double t;

            if (delta < 0)
            {
                return new Intersection(false, false, this, line, 0);
            }

            if(delta == 0)
            {
                t = (-B + Math.Sqrt(delta)) / (2 * A);
                if(t >= minDist && t <= maxDist)
                {
                    return new Intersection(true, true, this, line, t);
                }
                else
                {
                    return new Intersection(true, false, this, line, t);
                }
            }

            double t1 = (-B + Math.Sqrt(delta)) / (2 * A);
            double t2 = (-B - Math.Sqrt(delta)) / (2 * A);

            t = Math.Min(t1, t2);

            if (t >= minDist && t <= maxDist)
            {
                return new Intersection(true, true, this, line, t);
            }
            else
            {
                return new Intersection(true, false, this, line, t);
            }
        }

        public override Vector Normal(Vector v)
        {
            var n = v - Center;
            n.Normalize();
            return n;
        }
    }
}