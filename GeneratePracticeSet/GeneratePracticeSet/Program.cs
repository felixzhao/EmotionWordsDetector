using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace GeneratePracticeSet
{
    class Program
    {
        static void Main(string[] args)
        {
            string dir = ConfigurationManager.AppSettings["dir"];
            string outfile = ConfigurationManager.AppSettings["out"];

            var fileList = Directory.GetFiles(dir, "*.xml");

            StringBuilder outString = new StringBuilder();

            foreach (var file in fileList)
            {
                outString.Append(GetPracticeDocString(file));
                outString.AppendLine();
            }

            Write2File(outString.ToString(), outfile);

            Console.ReadKey();
        }

        private static string GetPracticeDocString(string sourcefile)
        {
            StringBuilder outString = new StringBuilder();

            XDocument xdoc = XDocument.Load(sourcefile);

            foreach (XElement sentence in xdoc.Descendants("sentence"))
            {
                foreach (XElement word in sentence.Descendants("word"))
                {
                    outString.Append(NodeGen(word));
                    outString.Append(" ");



                    var property = word.Attribute("property");
                    var emotion = word.Attribute("emotion");

                    Console.WriteLine("word :");
                    Console.WriteLine(word);

                    Console.WriteLine("property:" + property);
                    Console.WriteLine("emotion : " + emotion);
                    Console.WriteLine("Value : " + word.Value);
                }
            }

            return outString.ToString();
        }

        private static void Write2File(string outString, string outfilePath)
        {
            using (StreamWriter outfile = new StreamWriter(outfilePath))
            {
                outfile.Write(outString);
            }
        }

        private static string NodeGen(XElement word)
        {
            StringBuilder result = new StringBuilder();
            if (!string.IsNullOrEmpty(word.Value))
            {
                string emotion = word.Attribute("emotion").Value;
                string start = string.Empty;
                string end = string.Empty;
                if (emotion != "N/A")
                {
                    start = "{{";
                    end = "b\\" + emotion + "}}";
                }
                result.Append(start);
                result.Append(word.Attribute("property").Value);
                result.Append(end);
            }
            return result.ToString();
        }
    }
}
