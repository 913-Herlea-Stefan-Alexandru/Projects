using System;
using System.IO;

namespace VolumeRendering
{
    class Object3D
    {
        private string fileName;
        private int[,,] objectMatrix { get; set; }
        public int sizeX { get; }
        public int sizeY { get; }
        public int sizeZ { get; }

        public Object3D(string fileName, int sizeX, int sizeY, int sizeZ)
        {
            this.fileName = fileName;
            this.sizeX = sizeX;
            this.sizeY = sizeY;
            this.sizeZ = sizeZ;
            generateMatrix();
            if (this.sizeX > 160)
            {
                this.sizeX = 160;
            }
        }

        private void generateMatrix()
        {
            // byte[] bytes = File.ReadAllBytes("D:/VR/volume-renderer-913-Herlea-Stefan-Alexandru/VolumeRender/VolumeRendering/VolumeRendering/res/head-181x217x181.dat");
            objectMatrix = new int[sizeX, sizeY, sizeZ];
            using (FileStream fileStream = new FileStream(fileName, FileMode.Open))
            {
                for (int x = 0; x < sizeX; x++)
                {
                    for (int y = 0; y < sizeY; y++)
                    {
                        for (int z = 0; z < sizeZ; z++)
                        {
                            int data = fileStream.ReadByte();
                            if (data == -1)
                            {
                                Console.WriteLine("Cannot Read file!");
                                return;
                            }
                            objectMatrix[x, y, z] = data;
                        }
                    }
                }
            }
        }

        public bool isInside(Vector point)
        {
            return Convert.ToInt32(point.X) > 0 && Convert.ToInt32(point.Y) > 0 && Convert.ToInt32(point.Z) > 0 &&
                   Convert.ToInt32(point.X) < sizeX && Convert.ToInt32(point.Y) < sizeY && Convert.ToInt32(point.Z) < sizeZ;
        }

        public int getValue(Vector point)
        {
            if (!isInside(point))
            {
                return 0;
            }
            return objectMatrix[Convert.ToInt32(point.X), Convert.ToInt32(point.Y), Convert.ToInt32(point.Z)];
        }
    }
}
