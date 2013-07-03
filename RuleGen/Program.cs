using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Collections;
using System.Runtime.InteropServices;
using System.Xml;
using ICTCLASLib;
namespace RuleGen
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] argsList = Environment.GetCommandLineArgs();
            if (argsList.Length != 2)
            {
                Console.WriteLine("Usage: RuleGen <file name> or  RuleGen <directory name> ");
                return;
            }
            string[] fileList ;
            if (Directory.Exists(argsList[1]))
            {
                DirectoryInfo di = new DirectoryInfo(argsList[1]);
                fileList = Directory.GetFiles(argsList[1], "*.txt");
            }
            else if (File.Exists(argsList[1]))
            {
                fileList = new string[1];
                fileList[0] = argsList[1];
            }
            else{
                Console.WriteLine("Invalid file or directory name ");
                return;
            }
            if (!ICTCLAS.initialize())
            {
                Console.WriteLine("Initialize ICTCLAS libary failed!");
                return;
            }
            foreach (string fileName in fileList)
            {
                StreamReader rd = new StreamReader(fileName, Encoding.Default);
                string filedata = rd.ReadToEnd().Trim().Replace("\r\n", "");
                char[] delimiterChars = { '。', '！', '?' };
                string[] seArray = filedata.Split(delimiterChars);

                XmlTextWriter xmlWriter = null;
                int i = 1;
                int wordOffset = 1;
                foreach (string s in seArray)
                {

                    if (s != string.Empty)
                    {
                        ArrayList wordList = new ArrayList();
                        ICTCLAS.splitword(s, wordList);
                        if (xmlWriter == null)
                            xmlWriter = beginWriteXML(fileName);
                        writeWordsToXML(xmlWriter, wordList, i, ref wordOffset);

                    }
                    i++;
                }
                endWriteXML(xmlWriter);
            }
            ICTCLAS.uninitialize();
        }
        static XmlTextWriter beginWriteXML(string srcFileName)
        {
            FileInfo fileInfo = new FileInfo(srcFileName);
            string name = fileInfo.FullName.TrimEnd(fileInfo.Extension.ToCharArray());
            name += ".xml";
            XmlTextWriter xmlWriter = new XmlTextWriter(name, Encoding.Default);
            xmlWriter.Formatting = Formatting.Indented;
            xmlWriter.WriteStartDocument();
            xmlWriter.WriteStartElement("document");
            xmlWriter.WriteAttributeString("name", fileInfo.Name);
            return xmlWriter;
        }
        static void writeWordsToXML(XmlTextWriter wr, ArrayList wordList, int sentenceId, ref int wordOffset)
        {
            if (wr == null)
                return;
            if (wordList.Count == 0)
                return;
            wr.WriteStartElement("sentence");
            wr.WriteAttributeString("id", sentenceId.ToString());
            wr.WriteAttributeString("emotion", "N/A");
            foreach (SegWord word in wordList)
            {
                wr.WriteStartElement("word");
                wr.WriteAttributeString("id", wordOffset.ToString());
                int order = word.Number + 1;
                wr.WriteAttributeString("wordOrder", order.ToString());
                wr.WriteAttributeString("emotion", "N/A");
                if (word.wordType == "c" || word.wordType == "cc")
                {
                    wr.WriteAttributeString("conjunction", true.ToString());
                    wr.WriteAttributeString("effect", "same");
                }
                wr.WriteAttributeString("property", word.wordType);
                wr.WriteString(word.szWord);
                wr.WriteEndElement();
                wordOffset++;
            }
            wr.WriteEndElement();
        }
        static void endWriteXML(XmlTextWriter wr)
        {
            if (wr == null)
                return;
            wr.WriteEndElement();
            wr.WriteEndDocument();
            wr.Close();
        }

    }

}
