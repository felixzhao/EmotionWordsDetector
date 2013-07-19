using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace GenEvaluationData
{
    class Program
    {
        static void Main(string[] args)
        {
            string dir = @"e:\tagged-source\";
            string outpath = @"e:\sourceInfo.txt";
            string[] filePaths = Directory.GetFiles(dir, "*.xml");

            StringBuilder outString = new StringBuilder();

            foreach (var file in filePaths)
            {
                IList<string> temp = file.Split('\\');

                string filename = temp[temp.Count - 1].Replace(".xml", "");

                XDocument xdoc = XDocument.Load(file);

                foreach (XElement sentence in xdoc.Descendants("sentence"))
                {
                    foreach (XElement word in sentence.Descendants("word"))
                    {
                        if (word.Attribute("id") == null)
                        {
                            Console.WriteLine(filename);
                        }
                        else
                        {
                            string term = string.Format("{0},{1},{2};", filename, word.Attribute("id").Value, word.Attribute("emotion").Value);
                            outString.Append(term);
                        }
                    }
                }
            }

            Write2File(outpath, outString.ToString());

            Console.ReadKey();
        }

        private static void Write2File(string outpath,string outString)
        {
            using (StreamWriter outfile = new StreamWriter(outpath))
            {
                outfile.Write(outString);
            }
        }
    }
}
