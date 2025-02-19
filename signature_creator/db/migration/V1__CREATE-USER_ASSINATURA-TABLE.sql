CREATE TABLE user_assinatura(
    id_user VARCHAR2(11) NOT NULL,
    nome VARCHAR2(50) NOT NULL,
    cargo VARCHAR2(50) NOT NULL,
    empresa VARCHAR2(15) NOT NULL,
    telefone VARCHAR2(10),
    celular VARCHAR2(11) NOT NULL,
    email VARCHAR2(20) NOT NULL,
    PRIMARY KEY (id_user)
);
