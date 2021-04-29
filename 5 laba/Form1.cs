using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Drawing2D;
using System.Threading;
using System.IO;

namespace _5_laba
{
    public partial class Form1 : Form
    {
        static List<Point> pointsList = new List<Point>();
        public static double rotate(Point start, Point x, Point y)
        {
            return (x.X - start.X) * (y.Y - x.Y) - (x.Y - start.Y) * (y.X - x.X);
        }
        public static int skewProduct(Point A, Point B, Point C)
        {
            double skewProduct = (B.X - A.X) * (C.Y - A.Y) - (B.Y - A.Y) * (C.X - A.X);
            return skewProduct < 0 ? 1 : -1;
        }
        public class PointComparer : IComparer<Point>
        {
            public int Compare(Point x, Point y)
            {
                return rotate(pointsList[0], x, y) > 0 ? 1 : -1;
            }
        }      
        public void drawAxis(Graphics g)
        {
            SolidBrush q = new SolidBrush(Color.White);
            g.FillRectangle(q, 0, 0, pictureBox2.Width, pictureBox2.Height);
            g.TranslateTransform(pictureBox2.Width / 2, pictureBox2.Height / 2);
            g.DrawLine(Pens.Black, -pictureBox2.Size.Width / 2, 0, pictureBox2.Size.Width / 2, 0);
            g.DrawLine(Pens.Black, 0, -pictureBox2.Size.Height / 2, 0, pictureBox2.Size.Height / 2);
            g.DrawString("X", this.Font, Brushes.Black, pictureBox2.Size.Width / 2 - 20, -20);
            g.DrawString("Y", this.Font, Brushes.Black, 5, -pictureBox2.Size.Height / 2 + 5);
        }
        public Form1()
        {
            InitializeComponent();
        }
        private void GrahamsАlgorithm()
        {
            pictureBox2.Image = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            using (Graphics g = Graphics.FromImage(pictureBox2.Image))
            {
                drawAxis(g);
                SolidBrush pointPen = new SolidBrush(Color.Red);
                for (int i = 0; i < pointsList.Count; i++)
                {
                    g.FillEllipse(pointPen, pointsList[i].X - 3, pointsList[i].Y - 3, 5, 5);
                }
            }
            // Test data.
            //Point vertex1 = new Point(-5, -71);
            //Point vertex2 = new Point(-3, -33);
            //Point vertex3 = new Point(50, -57);
            //Point vertex4 = new Point(76, -73);
            //Point vertex5 = new Point(84, -28);
            //Point vertex6 = new Point(44, 36);
            //Point vertex7 = new Point(-65, -23);
            //Point vertex8 = new Point(-35, 30);

            //pointsList.Add(vertex1);
            //pointsList.Add(vertex2);
            //pointsList.Add(vertex3);
            //pointsList.Add(vertex4);
            //pointsList.Add(vertex5);
            //pointsList.Add(vertex6);
            //pointsList.Add(vertex7);
            //pointsList.Add(vertex8);          

            Point leftDownPoint = new Point(pointsList[0].X, pointsList[0].Y);          
            for (int i = 0; i < pointsList.Count; i++)
            {
                if (pointsList[i].X < leftDownPoint.X)
                    leftDownPoint = pointsList[i];
                if (pointsList[i].X == leftDownPoint.X)
                    leftDownPoint = pointsList[i].Y > leftDownPoint.Y ? pointsList[i] : leftDownPoint;
            }           

            for (int i = 0; i < pointsList.Count; i++)
            {
                if (pointsList[i].X == leftDownPoint.X && pointsList[i].Y == leftDownPoint.Y)
                {
                    var tempPoint = pointsList[0];
                    pointsList[0] = leftDownPoint;
                    pointsList[i] = tempPoint;
                }
            }

            PointComparer comp = new PointComparer();         
            pointsList.Sort(1, pointsList.Count - 1, comp);
           
            using (Graphics g = Graphics.FromImage(pictureBox2.Image))
            {
                g.TranslateTransform(pictureBox2.Width / 2, pictureBox2.Height / 2);
                SolidBrush pointPen = new SolidBrush(Color.Red);
                for (int i = 0; i < pointsList.Count; i++)
                {
                    g.FillEllipse(pointPen, pointsList[i].X - 3, pointsList[i].Y - 3, 5, 5);
                }
                Stack<Point> st = new Stack<Point>();
                st.Push(pointsList[0]);
                st.Push(pointsList[1]);
                Thread.Sleep(1000);
                g.DrawLine(Pens.Black, st.ElementAt(0), st.ElementAt(1));
                pictureBox2.Refresh();
                for (int i = 2; i < pointsList.Count; i++)
                {
                    Thread.Sleep(1000);
                    while (skewProduct(st.ElementAt(1), st.Peek(), pointsList[i]) < 0)
                    {
                        g.DrawLine(Pens.White, st.Peek(), st.ElementAt(1));
                        st.Pop();
                    }
                    g.DrawLine(Pens.Black, st.ElementAt(0), pointsList[i]);
                    st.Push(pointsList[i]);                    
                    pictureBox2.Refresh();
                }
                Thread.Sleep(1000);
                g.DrawLine(Pens.Black, pointsList[0], st.Peek());
                pictureBox2.Refresh();
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox2.Image = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            Graphics g = Graphics.FromImage(pictureBox2.Image);
            drawAxis(g);     
        }

        private void button1_Click(object sender, EventArgs e)
        {
            GrahamsАlgorithm();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Point tempPoint = new Point();
            tempPoint.X = Convert.ToInt32(textBox1.Text);
            tempPoint.Y = Convert.ToInt32(textBox2.Text) * -1;
            pointsList.Add(tempPoint);
            pictureBox2.Image = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            using (Graphics g = Graphics.FromImage(pictureBox2.Image))
            {
                drawAxis(g);
                SolidBrush pointPen = new SolidBrush(Color.Red);
                for (int i = 0; i < pointsList.Count; i++)
                {
                    g.FillEllipse(pointPen, pointsList[i].X - 3, pointsList[i].Y - 3, 5, 5);
                }
            }
            textBox1.Text = "";
            textBox2.Text = "";
        }
    }
}
