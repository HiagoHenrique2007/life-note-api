CREATE TABLE record(
  id INT PRIMARY KEY AUTO INCREMENT,
  customer_id INT FOREIGN KEY NOT NULL,
  feeling ENUM('bom', 'neutro', 'mal') NOT NULL,
  emotion TEXT,
  record_text TEXT
  created_at TEXT
);

CREATE TABLE customers(
  id INT PRIMARY KEY AUTO INCREMENT,
  customer_name TEXT NOT NULL,
  customer_password TEXT NOT NULL,
  created_at TEXT
);