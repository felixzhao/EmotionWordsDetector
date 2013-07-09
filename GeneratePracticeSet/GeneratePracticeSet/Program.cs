using System;
using System.Collections.Generic;
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
            StringBuilder outString = new StringBuilder();

            XDocument xdoc = XDocument.Load(@"E:\6.xml");

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

            Write2File(outString.ToString());

            Console.ReadKey();
        }

        private static void Write2File(string outString)
        {
            using (StreamWriter outfile = new StreamWriter(@"E:\6_1.txt"))
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
                    end = " \\" + emotion + "}}";
                }
                result.Append(start);
                result.Append(word.Attribute("property").Value);
                result.Append(end);
            }
            return result.ToString();
        }
    }
}
