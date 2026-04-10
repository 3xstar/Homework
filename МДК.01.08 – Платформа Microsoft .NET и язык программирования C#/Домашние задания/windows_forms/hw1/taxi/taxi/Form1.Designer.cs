namespace taxi
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            button1 = new Button();
            tableLayoutPanel1 = new TableLayoutPanel();
            comboBox1 = new ComboBox();
            label1 = new Label();
            checkedListBox1 = new CheckedListBox();
            label2 = new Label();
            pictureBox2 = new PictureBox();
            pictureBox1 = new PictureBox();
            label3 = new Label();
            label4 = new Label();
            tableLayoutPanel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // button1
            // 
            button1.BackColor = Color.Gold;
            button1.Dock = DockStyle.Bottom;
            button1.Font = new Font("Segoe UI", 20F, FontStyle.Bold);
            button1.ForeColor = Color.DimGray;
            button1.Location = new Point(25, 556);
            button1.Margin = new Padding(50);
            button1.Name = "button1";
            button1.Size = new Size(434, 80);
            button1.TabIndex = 0;
            button1.Text = "ЗАКАЗАТЬ ТАКСИ";
            button1.UseVisualStyleBackColor = false;
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.ColumnCount = 4;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            tableLayoutPanel1.Controls.Add(comboBox1, 1, 0);
            tableLayoutPanel1.Controls.Add(label1, 0, 0);
            tableLayoutPanel1.Controls.Add(checkedListBox1, 1, 1);
            tableLayoutPanel1.Controls.Add(label2, 0, 1);
            tableLayoutPanel1.Controls.Add(pictureBox2, 3, 1);
            tableLayoutPanel1.Controls.Add(pictureBox1, 3, 0);
            tableLayoutPanel1.Controls.Add(label3, 0, 2);
            tableLayoutPanel1.Controls.Add(label4, 1, 2);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.Location = new Point(25, 25);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 3;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 33.3333321F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            tableLayoutPanel1.Size = new Size(434, 531);
            tableLayoutPanel1.TabIndex = 2;
            // 
            // comboBox1
            // 
            comboBox1.AllowDrop = true;
            comboBox1.Anchor = AnchorStyles.None;
            tableLayoutPanel1.SetColumnSpan(comboBox1, 2);
            comboBox1.Font = new Font("Segoe UI", 20F);
            comboBox1.ImeMode = ImeMode.NoControl;
            comboBox1.Items.AddRange(new object[] { "Эконом", "Комфорт", "Комфорт+", "Бизнес" });
            comboBox1.Location = new Point(147, 66);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(138, 45);
            comboBox1.TabIndex = 3;
            // 
            // label1
            // 
            label1.Anchor = AnchorStyles.None;
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 20F, FontStyle.Bold);
            label1.Location = new Point(7, 70);
            label1.Name = "label1";
            label1.Size = new Size(93, 37);
            label1.TabIndex = 0;
            label1.Text = "Класс";
            // 
            // checkedListBox1
            // 
            tableLayoutPanel1.SetColumnSpan(checkedListBox1, 2);
            checkedListBox1.Dock = DockStyle.Fill;
            checkedListBox1.Font = new Font("Segoe UI", 9F);
            checkedListBox1.FormattingEnabled = true;
            checkedListBox1.Items.AddRange(new object[] { "Детское кресло", "Перевозка животных", "Перевозка груза", "Кондиционер в салоне", "Зарядка телефона", "Эвакуация автомобиля", "Дополнительное ожидание", "Остановка вне маршрута", "Терминал для оплаты" });
            checkedListBox1.Location = new Point(111, 180);
            checkedListBox1.Name = "checkedListBox1";
            checkedListBox1.Size = new Size(210, 171);
            checkedListBox1.TabIndex = 4;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.None;
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 19F, FontStyle.Bold);
            label2.Location = new Point(5, 229);
            label2.Name = "label2";
            label2.Size = new Size(98, 72);
            label2.TabIndex = 5;
            label2.Text = "Доп.\r\nуслуги\r\n";
            // 
            // pictureBox2
            // 
            pictureBox2.BackgroundImageLayout = ImageLayout.None;
            pictureBox2.Dock = DockStyle.Fill;
            pictureBox2.Image = (Image)resources.GetObject("pictureBox2.Image");
            pictureBox2.Location = new Point(327, 180);
            pictureBox2.Name = "pictureBox2";
            pictureBox2.Size = new Size(104, 171);
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.TabIndex = 6;
            pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            pictureBox1.BackgroundImageLayout = ImageLayout.None;
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(327, 3);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(104, 171);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.TabIndex = 2;
            pictureBox1.TabStop = false;
            // 
            // label3
            // 
            label3.Anchor = AnchorStyles.None;
            label3.AutoSize = true;
            label3.Font = new Font("Segoe UI", 24F, FontStyle.Bold);
            label3.Location = new Point(4, 420);
            label3.Name = "label3";
            label3.Size = new Size(100, 45);
            label3.TabIndex = 7;
            label3.Text = "Цена";
            // 
            // label4
            // 
            label4.Anchor = AnchorStyles.None;
            label4.AutoSize = true;
            tableLayoutPanel1.SetColumnSpan(label4, 3);
            label4.Font = new Font("Segoe UI", 30F, FontStyle.Bold);
            label4.ForeColor = Color.ForestGreen;
            label4.Location = new Point(148, 415);
            label4.Name = "label4";
            label4.Size = new Size(245, 54);
            label4.TabIndex = 8;
            label4.Text = "100 рублей";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.Khaki;
            ClientSize = new Size(484, 661);
            Controls.Add(tableLayoutPanel1);
            Controls.Add(button1);
            Name = "Form1";
            Padding = new Padding(25);
            Text = "Form1";
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Button button1;
        private TableLayoutPanel tableLayoutPanel1;
        private Label label1;
        private PictureBox pictureBox1;
        private ComboBox comboBox1;
        private CheckedListBox checkedListBox1;
        private Label label2;
        private PictureBox pictureBox2;
        private Label label3;
        private Label label4;
    }
}
