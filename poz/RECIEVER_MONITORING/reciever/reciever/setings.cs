using System;
using System.Collections.Generic;
using System.ComponentModel;
//using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Xml;
using System.IO;
using System.IO.Compression;
using System.Data.OleDb;
using System.Data;
using System.Xml.Serialization;

using System.Threading;

using System.Net;
using System.Net.Sockets;
using System.Diagnostics;

namespace reciever
{
    public partial class setings : Form
    {
        //Настройки
        ini nastr = new ini();
        XmlWriterSettings settings = new XmlWriterSettings();
        XmlTextReader rdr = new XmlTextReader("Settings.xml");
        //Настройки

        //Массив файлов источника
        public string[] files_source;
        //Массив новых файлов источника
        public string[] new_files_source;
        //Массив файлов приемника
        public string[] files_destination;
        //Текущий time
        public string current_time;
        //Сообщение
        string message = " ";
        //Статистика
        int save_records;
        double save_percent;
        //Копия размера буфера чтения
        int backup_buffer_size;
        //сервер для передачи времянки
        //Thread serverth = new Thread(Go);
        //serverth.Priority = ThreadPriority.Lowest;

        //Пауза
        public bool pause_cycle = true;
        //Time
        dep time = new dep();
        //Store
        dep store = new dep();




        public setings()
        {
            InitializeComponent();
            
            //serverth.Start();
            //serverth.Join();
            //var stopwatch = Stopwatch.StartNew();
            //stopwatch = Stopwatch.StartNew();
            //Thread.Sleep(0);
            //stopwatch.Stop(); server.Go();
        }

        //Сервер TCP
        Byte[] bytes = new Byte[8192];
        String data = null;
        TcpListener server;
        String answer = "SUCK";

        public void Go()
        {
            //TcpListener server = null;
            
                // Set the TcpListener on port 255.
                Int32 port = 255;
                IPAddress localAddr = IPAddress.Parse("127.0.0.1");

                // TcpListener server = new TcpListener(port);
                server = new TcpListener(IPAddress.Any, port);

                // Start listening for client requests.
                server.Start();
                //timer4.Enabled = true;

                // Buffer for reading data
                
                //backgroundWorker1 = new BackgroundWorker();
                //backgroundWorker1.DoWork += new DoWorkEventHandler(backgroundWorker1_DoWork);
                
                //backgroundWorker1.WorkerReportsProgress = true;
                //backgroundWorker1.WorkerSupportsCancellation = true;
                backgroundWorker1.RunWorkerAsync();
            }

        public void Go_Next(){


                // Enter the listening loop.
                //while (true)
                //{
                    //Console.Write("Waiting for a connection... ");

                    Application.DoEvents();
                    //Thread.Sleep(5000);
                    Application.DoEvents();
                    //if (backgroundWorker1.CancellationPending)
                    //    return;
                    // Perform a blocking call to accept requests.
                    // You could also user server.AcceptSocket() here.
                    TcpClient client = server.AcceptTcpClient();
                    MessageBox.Show("Connected!");

                    data = null;

                    // Get a stream object for reading and writing
                    NetworkStream stream = client.GetStream();

                    int i;

                    // Loop to receive all the data sent by the client.
                    while ((i = stream.Read(bytes, 0, bytes.Length)) != 0)
                    {
                        // Translate data bytes to a ASCII string.
                        data = System.Text.Encoding.ASCII.GetString(bytes, 0, i);
                        MessageBox.Show("Received: {0}", data);

                        // Process the data sent by the client.
                        data = data.ToUpper();

                        byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

                        // Send back a response.
                        stream.Write(msg, 0, msg.Length);
                        MessageBox.Show("Sent: {0}", data);
                    }
                //}
            
            }



        private void выходToolStripMenuItem_Click(object sender, EventArgs e)
        {
            timer2.Stop();
            save_set();
            notifyIcon1.Visible = false;
            Application.Exit();
            Environment.Exit(0);
        }

        //Cохранение настроек
        public void save_set()
        {

            nastr.source_path = textBox1.Text;
            nastr.destination_path = textBox2.Text;
            nastr.current_time_name = comboBox1.Text;
            nastr.wr_time = checkBox2.Checked.ToString();
            nastr.loading_store = checkBox1.Checked.ToString();
            nastr.wr_store = checkBox3.Checked.ToString();
            nastr.pause_sec = (Math.Ceiling((double)numericUpDown1.Value)).ToString();
            nastr.buffer_zap = (Math.Ceiling((double)numericUpDown2.Value)).ToString();


            settings.Indent = true;
            settings.IndentChars = ("    ");
            using (XmlWriter writer = XmlWriter.Create("Settings.xml", settings))
            {
                // Write XML time.
                writer.WriteStartElement(nastr.Sect);
                writer.WriteElementString("source_path", nastr.source_path);
                writer.WriteElementString("destination_path", nastr.destination_path);
                writer.WriteElementString("current_time_name", nastr.current_time_name);
                writer.WriteElementString("wr_time", nastr.wr_time);
                writer.WriteElementString("loading_store", nastr.loading_store);
                writer.WriteElementString("wr_store", nastr.wr_store);
                writer.WriteElementString("pause_sec", nastr.pause_sec);
                writer.WriteElementString("buffer_zap", nastr.buffer_zap);
                writer.WriteEndElement();
                writer.Flush();
                writer.Close();
            }
        }

        //Чтение настроек
        public void read_set()
        {

            ////ini файл

            while (rdr.Read())
            {

                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "source_path")
                {
                    rdr.Read();
                    textBox1.Text = rdr.Value.ToString();

                }
                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "destination_path")
                {
                    rdr.Read();
                    textBox2.Text = rdr.Value.ToString();

                }
                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "current_time_name")
                {
                    rdr.Read();
                    comboBox1.Text = rdr.Value.ToString();
                    //comboBox1.SelectedItem = comboBox1.Text;
                }


                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "wr_time")
                {
                    rdr.Read();
                    checkBox2.Checked = Convert.ToBoolean(rdr.Value);

                }
                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "loading_store")
                {
                    rdr.Read();
                    checkBox1.Checked = Convert.ToBoolean(rdr.Value);

                }
                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "wr_store")
                {
                    rdr.Read();
                    checkBox3.Checked = Convert.ToBoolean(rdr.Value);

                }
                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "pause_sec")
                {
                    rdr.Read();
                    numericUpDown1.Value = Convert.ToInt16(rdr.Value);

                }

                if (rdr.NodeType == XmlNodeType.Element && rdr.Name == "buffer_zap")
                {
                    rdr.Read();
                    numericUpDown2.Value = Convert.ToInt16(rdr.Value);

                }

            }
            rdr.Close();
            if (textBox1.Text == "" | textBox1.Text == "\r\n    ") { textBox1.Text = @"C:\"; }
            comboBox1.Items.Clear();
            time.error = "";
            try
            {
                files_source = Directory.GetFiles(textBox1.Text, "Time_*.dep");



                foreach (string value in files_source)
                {
                    comboBox1.Items.Add(Path.GetFileNameWithoutExtension(value));
                    //comboBox1.Text = Path.GetFileName(value);
                }
            }
            catch (IOException err) { time.error = err.ToString(); }
        }


        private void настройкиToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Остановка закачки
            show_load_bad();
            timer2.Stop();
            //Скрываем статистику если она открыта
            // try
            // {
            //     //stat.Hide();
            //}catch{}

            read_set();
            this.Show();
            this.Focus();
            this.WindowState = FormWindowState.Normal;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Hide();
            Go();


        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            notifyIcon1.Visible = false;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            save_set();
            e.Cancel = true;
            this.Hide();


        }


        private void button1_Click(object sender, EventArgs e)
        {
            DialogResult result = folderBrowserDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                textBox1.Text = folderBrowserDialog1.SelectedPath;
                files_source = Directory.GetFiles(textBox1.Text, "Time_*.dep");
                comboBox1.Items.Clear();
                comboBox1.Text = "";
                foreach (string value in files_source)
                {
                    comboBox1.Items.Add(Path.GetFileNameWithoutExtension(value));
                    comboBox1.SelectedItem = Path.GetFileNameWithoutExtension(value);
                }



            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult result = folderBrowserDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                textBox2.Text = folderBrowserDialog1.SelectedPath;
                Application.DoEvents();
                files_destination = Directory.GetFiles(textBox2.Text, "Time_*.dep");
            }
        }



        private void button3_Click(object sender, EventArgs e)
        {
            this.Hide();

        }

        private void статистикаToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Hide();
            //stat.ShowDialog(this);

            //if (stat.DialogResult == DialogResult.OK)
            //{ 
            //}
        }
        //Переключение значков в трее
        bool trig = false;
        private void timer1_Tick(object sender, EventArgs e)
        {
            Application.DoEvents();
            if (trig)
            {
                notifyIcon1.Icon = (System.Drawing.Icon)reciever.Properties.Resources.ball_green1;
                trig = false;
            }
            else
            {
                notifyIcon1.Icon = (System.Drawing.Icon)reciever.Properties.Resources.ball_yellow1;

                trig = true;
            }
        }

        private void стартToolStripMenuItem_Click(object sender, EventArgs e)
        {
            read_set();
            this.Hide();
            //stat.Hide();

            //Time
            current_time = comboBox1.Text;
            time.src = textBox1.Text;
            time.dst = textBox2.Text;
            time.time = current_time;
            time.now_src_numbs_record = (int)numericUpDown2.Value;

            //Store
            store.src = textBox1.Text;
            store.dst = textBox2.Text;
            store.time = "STORE";
            store.now_src_numbs_record = (int)numericUpDown2.Value;


            backup_buffer_size = (int)numericUpDown2.Value;

            timer2.Interval = (int)numericUpDown1.Value;
            nastr.pause_sec = (timer2.Interval).ToString();

            //if (time.src == "" | time.dst == "" | time.time == "")
            //{
            //    show_load_bad();
            //}
            //else
            //{

            show_load_good();
            timer2.Start();
            //}
        }

        //Закачка Бэд
        public void show_load_bad()
        {
            timer1.Stop();
            notifyIcon1.Icon = (System.Drawing.Icon)reciever.Properties.Resources.ball_red1;
        }
        //Закачка Гуд
        public void show_load_good()
        {
            timer1.Start();
        }

        private void стопToolStripMenuItem_Click(object sender, EventArgs e)
        {
            timer2.Stop();
            show_load_bad();

        }

        //Проверка нового файла
        public void check_new_file()
        {
            try
            {
                //Список файлов источника
                new_files_source = Directory.GetFiles(textBox1.Text, "Time_*.dep");

                //Список файлов приемника
                files_destination = Directory.GetFiles(textBox2.Text, "Time_*.dep");
                string new_time = "";
                comboBox1.SelectedItem = comboBox1.Text;
                //if (comboBox1.SelectedIndex == -1) { comboBox1.SelectedIndex = comboBox1.Items.Count-1; }
                //Если файла в приемнике нет, то закачиваем его, иначе последний файл
                for (int i = comboBox1.SelectedIndex; i < new_files_source.Count(); i++)
                {
                    Application.DoEvents();
                    string p = textBox2.Text + "\\" + Path.GetFileName(new_files_source[i]);
                    if (!File.Exists(p))
                    {
                        new_time = new_files_source[i];
                        comboBox1.Text = Path.GetFileNameWithoutExtension(new_time);
                        comboBox1.SelectedItem = comboBox1.Text;
                        current_time = comboBox1.Text;
                        time.time = current_time;
                        notifyIcon1.Visible = false;
                        notifyIcon1.Visible = true;
                        notifyIcon1.ShowBalloonTip(2000, "Текущий файл:", current_time, ToolTipIcon.Info);

                        break;
                    }
                    else
                    {
                        new_time = new_files_source[new_files_source.Count() - 1];
                        comboBox1.Text = Path.GetFileNameWithoutExtension(new_time);
                        comboBox1.SelectedItem = comboBox1.Text;
                        current_time = comboBox1.Text;
                        time.time = current_time;
                    }
                }
                //Если новый файл
                if ((String.Compare(current_time, Path.GetFileNameWithoutExtension(new_time))) != 0)
                {
                    current_time = Path.GetFileNameWithoutExtension(new_time);
                    time.time = current_time;
                    comboBox1.Text = current_time;

                    comboBox1.Items.Add(Path.GetFileNameWithoutExtension(new_time));
                    comboBox1.SelectedItem = comboBox1.Text;
                    notifyIcon1.Visible = false;
                    notifyIcon1.Visible = true;
                    notifyIcon1.ShowBalloonTip(2000, "Текущий файл:", current_time, ToolTipIcon.Info);
                    //save_set();

                }


            }
            catch (IOException err) { time.error = err.ToString(); }

        }

        //Пересылка
        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2.Stop();


            store_read_write();

            //Ошибка чтения
            time.error = "";

            ////Кол-во записей для четния(записи) за один раз 
            time.now_src_numbs_record = backup_buffer_size;
            //Число записей в lst файле источника
            if (time.error == "")
            {
                time.calc_src_numbs_record();
            }
            else { return; }
            //Application.DoEvents();
            //Число записей в lst файле приемника
            if (time.error == "")
            {
                time.calc_dst_numbs_record();
            }
            else { return; }
            Application.DoEvents();
            save_records = time.dst_numbs_record;
            save_percent = Math.Round(((double)save_records / time.src_numbs_record) * 100, 1);
            notifyIcon1.Text = current_time + ": \n" + save_records + "/" + time.src_numbs_record +
            "\n  " + save_percent + "%";



            //Проверка нового файла
            if (time.src_numbs_record <= time.dst_numbs_record)
            {

                check_new_file();
                timer2.Start();
                return;

            }
            else
            {


                //Считываем запись 21 байт из lst источника по номеру
                //time.numb_cur_lst_record = time.dst_numbs_record;
                time.numb_cur_lst_record = time.dst_numbs_record;

                if ((time.numb_cur_lst_record) < (time.src_numbs_record))
                {
                    if (time.error == "")
                    {
                        time.src_read_lst_record();
                    }
                    else { return; }
                    //Application.DoEvents();
                    //Считываем запись из dep источника 
                    if (time.error == "")
                    {
                        time.src_read_dep_record();
                    }
                    else { return; }
                    //Application.DoEvents();

                    //Запись lst запись в приемник
                    if (time.error == "")
                    {
                        time.dst_write_lst_record();
                    }
                    else { return; }
                    //Application.DoEvents();
                    //Запись dep записи в приемник
                    if (time.error == "")
                    {
                        time.dst_write_dep_record();
                    }
                    else { return; }
                    //Application.DoEvents();
                    //Cтатистика
                    //save_records=time.numb_cur_lst_record+time.now_src_numbs_record;
                    //save_percent=Math.Round(((double)save_records/time.src_numbs_record)*100,1);
                    //notifyIcon1.Text = current_time + ": \n" + save_records + "/" + time.src_numbs_record+
                    //"\n  "+ save_percent+"%";



                }
            }

            timer2.Start();
        }

        //Чтение запись Store
        public void store_read_write()
        {


            //Ошибка чтения
            store.error = "";

            ////Кол-во записей для чтения(записи) за один раз 

            store.now_src_numbs_record = backup_buffer_size;
            //Число записей в lst файле источника
            if (store.error == "")
            {
                store.calc_src_numbs_record();
            }
            else { return; }
            //Application.DoEvents();
            //Число записей в lst файле приемника
            if (store.error == "")
            {
                store.calc_dst_numbs_record();
            }
            else { return; }
            Application.DoEvents();
            //save_records = store.dst_numbs_record;
            //save_percent = Math.Round(((double)save_records / store.src_numbs_record) * 100, 1);
            //notifyIcon1.Text = current_store + ": \n" + save_records + "/" + store.src_numbs_record +
            //"\n  " + save_percent + "%";

            //Проверка нового файла
            if (store.src_numbs_record <= store.dst_numbs_record)
            {

                //check_new_file();
                return;

            }
            else
            {


                //Считываем запись 21 байт из lst источника по номеру
                //store.numb_cur_lst_record = time.dst_numbs_record;
                store.numb_cur_lst_record = store.dst_numbs_record;

                if ((store.numb_cur_lst_record) < (store.src_numbs_record))
                {
                    if (store.error == "")
                    {
                        store.src_read_lst_record();
                    }
                    else { return; }
                    //Application.DoEvents();
                    //Считываем запись из dep источника 
                    if (store.error == "")
                    {
                        store.src_read_dep_record();

                    }
                    else { return; }
                    //Application.DoEvents();

                    //Запись lst запись в приемник
                    if (store.error == "")
                    {
                        store.dst_write_lst_record();
                    }
                    else { return; }
                    //Application.DoEvents();
                    //Запись dep записи в приемник
                    if (store.error == "")
                    {
                        store.dst_write_dep_record();
                    }
                    else
                    { return; }

                }
            }

        }

        private void notifyIcon1_MouseClick(object sender, MouseEventArgs e)
        {

            //notifyIcon1.ShowBalloonTip(2);
            //notifyIcon1.

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void setings_MouseEnter(object sender, EventArgs e)
        {
            //notifyIcon1.BalloonTipText = current_time + ": " + time.numb_cur_lst_record + " из" + time.now_src_numbs_record;
            //notifyIcon1.ShowBalloonTip(3);
        }

        private void setings_MouseLeave(object sender, EventArgs e)
        {
            //notifyIcon1.BalloonTipShown();
        }

        private void comboBox1_DropDownClosed(object sender, EventArgs e)
        {
            current_time = comboBox1.Text;
            checkBox2.Text = comboBox1.Text;
            comboBox1.SelectedItem = comboBox1.Text;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            //Сжатие базы LogsBuilder C:\Program Files\Common Files\PS Shared\Database в
            // C:\Program Files\Common Files\PS Shared\Database\reciever
            //FileStream fsInput = File.OpenRead(@"C:\Program Files\Common Files\PS Shared\Database\WELLSITEDB.mdb");
            //FileStream fsOutput = File.Create(@"C:\Program Files\Common Files\PS Shared\Database\WELLSITEDB.zip");
            try
            {
                File.Copy(@"C:\Program Files\\Common Files\PS Shared\Database\WELLSITEDB.mdb", @"C:\Program Files\Common Files\PS Shared\Database\Archive\test.mdb", true);
                FileStream fsInput = File.OpenRead(@"C:\Program Files\Common Files\PS Shared\Database\Archive\test.mdb");
                FileStream fsOutput = File.Create(@"C:\Program Files\Common Files\PS Shared\Database\Archive\WELLSITEDB.gz");
                GZipStream gzipStream = new GZipStream(fsOutput, CompressionMode.Compress);
                Byte[] buffer = new Byte[fsInput.Length];
                int h;
                while ((h = fsInput.Read(buffer, 0, buffer.Length)) > 0)
                {
                     gzipStream.Write(buffer, 0, h);
                }
            }
            catch{
            }
            /*//Чтение базы
            string connectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Program Files\Common Files\PS Shared\Database\WELLSITEDB.mdb";  
            string strSQL = "SELECT * FROM messageData";
            byte[] komment ;
                // Create a connection  
                using (OleDbConnection connection = new OleDbConnection(connectionString))
                {
                    // Create a command and set its connection  
                    OleDbCommand command = new OleDbCommand(strSQL, connection);
                    // Open the connection and execute the select command.  
                    try
                    {
                        // Open connecton  
                        connection.Open();
                        
                        // Execute command  
                        using (OleDbDataReader reader = command.ExecuteReader())
                        {
                            int ColumnCount = reader.FieldCount;
                            string ListOfColumns = string.Empty;
                            while (reader.Read())
                            {

                                komment = reader["objImage"] as byte[];
                                textBox3.Text += komment;

                                for (int i = 0; i <= ColumnCount - 1; i++)
                                {
                                    ListOfColumns = ListOfColumns + reader[i].ToString() + "|";
                                }

                                ListOfColumns = ListOfColumns + System.Environment.NewLine;
                            }
                            TextWriter tw = new StreamWriter(@"suck.txt");
                            tw.WriteLine(ListOfColumns);
                            tw.Close();

                        }
                        
                    }
                    catch (Exception ex)
                    {
                        
                    }
                    // The connection is automatically closed becasuse of using block.
             */
            /*
            OleDbConnection connection = new OleDbConnection();
			
			//Строка соединения с БД, котороя содержит провайдера для
			//подключения и имя базы данных,
			//которая будет находиться рядом с исполняемым файлом.
			connection.ConnectionString =
                "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + @"C:\Program Files\Common Files\PS Shared\Database\WELLSITEDB.mdb";
			
			//Инициализируем новую переменну
			//содержащую комманду - запрос
			OleDbCommand command = new OleDbCommand();
			
			//Текст комманды-запроса к базе данных
			command.CommandText = "Select * from messageData";
			
			//Задаем подключение System.Data.OleDb.OleDbConnection,
			//используемое экземпляром класса System.Data.OleDb.OleDbCommand.
			command.Connection = connection;
            byte[] arr;
            
                //Открываем новое подключение к базе данных со значениями свойств,
                //определяемыми объектом
                //System.Data.OleDb.OleDbConnection.ConnectionString.
                connection.Open();

                //Отправляет System.Data.OleDb.OleDbCommand.CommandText
                //в System.Data.OleDb.OleDbCommand.Connection
                //и создает объект System.Data.OleDb.OleDbDataReader.
                OleDbDataReader dr = command.ExecuteReader();

                //Значение true, если объект System.Data.OleDb.OleDbDataReader
                //содержит одну или несколько строк;
                //в противном случае — значение false.


                /*if (dr.HasRows)
                {
                    //
                    while (dr.Read())
                    {


                        
                        arr = dr["objImage"] as byte[];
                        int a = 200;
                        File.WriteAllBytes("suck.txt", arr);
                        textBox3.Text += arr.GetValue(0);
                    }
                }
          

                    foreach (DataColumnCollection dt in dr)
                    {
                    textBox3.Text += dt;}
              
                //using (FileStream file_stream = new FileStream("objImage_suck.bin", FileMode.Create))
            //{
            //    using (BinaryWriter writer = new BinaryWriter(file_stream))
            //    {
            //        writer.Write(arr);
            //        writer.Close();
            //    }
                   
            //}
            timer3.Stop();
               */

        }

       

        

        private void backgroundWorker1_DoWork_1(object sender, DoWorkEventArgs e)
        {
            while (true)
            {
                //Console.Write("Waiting for a connection... ");

                //Application.DoEvents();
                //Thread.Sleep(5000);
                //Application.DoEvents();
                //if (backgroundWorker1.CancellationPending)
                //    return;
                // Perform a blocking call to accept requests.
                // You could also user server.AcceptSocket() here.
                TcpClient client = server.AcceptTcpClient();
                //MessageBox.Show("Connected!");

                data = null;

                // Get a stream object for reading and writing
                NetworkStream stream = client.GetStream();

                int i;

                // Loop to receive all the data sent by the client.
                while ((i = stream.Read(bytes, 0, bytes.Length)) != 0)
                {
                    // Translate data bytes to a ASCII string.
                    data = System.Text.Encoding.ASCII.GetString(bytes, 0, i);
                    //MessageBox.Show("Received: {0}", data);



                    if (data.ToString() !=""){

                        if (time.back_dep_rec.Length != 0)
                        {
                            answer = System.Text.Encoding.ASCII.GetString(time.back_dep_rec);
                        }
                        MessageBox.Show(' '+ data.ToString()+','+ time.src.ToString()+','+ time.time +','+time.src_numbs_record);
                    }

                    // Process the data sent by the client.
                    if (data.ToString()=="T CUR"){
                            
                        //answer = data.ToUpper();

                        if (time.back_dep_rec.Length!=0){
                        answer = System.Text.Encoding.ASCII.GetString(time.back_dep_rec);
                        }
                    }


                    
                    //Текст в массив байт посылка
                    byte[] msg = System.Text.Encoding.ASCII.GetBytes(answer);

                    // Send back a response.

                    stream.Write(msg, 0, msg.Length);
                    //MessageBox.Show("Sent: {0}", data);
                }
            }
        }
    }
}
