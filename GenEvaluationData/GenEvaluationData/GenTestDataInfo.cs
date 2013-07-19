using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Xml.Linq;

namespace GenEvaluationData
{
    public class GenTestDataInfo
    {
        public int AP { get; set; }
        public int AN { get; set; }

        public GenTestDataInfo(string dir)
        {
            string[] filePaths = Directory.GetFiles(dir, "*.xml");
        }

        public string GetTaggedInfoFromFile(string file)
        {
            string result = string.Empty;

            IList<string> temp = file.Split('\\');

            string filename = temp[temp.Count -1].Replace(".xml","");

            StringBuilder outString = new StringBuilder();

            XDocument xdoc = XDocument.Load(file);

            foreach (XElement sentence in xdoc.Descendants("sentence"))
            {
                foreach (XElement word in sentence.Descendants("word"))
                {
                    string term = string.Format("{0},{1},{2};", filename,word.Attribute("id").Value, word.Attribute("emotion").Value);
                    outString.Append(term);
                }
            }

            return result;
        }
    }
}
