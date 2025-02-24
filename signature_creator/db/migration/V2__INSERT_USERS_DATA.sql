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

ALTER TABLE user_assinatura 
    RENAME COLUMN email TO email_user;

ALTER TABLE user_assinatura 
    MODIFY (empresa VARCHAR2(25));


INSERT INTO user_assinatura VALUES('06233247250', 'PEDRO HENRIQUE RODRIGUES DE SÁ', 'AUXILIAR DE TI', 'Mônaco Motocenter', '9130758492', '91985454007', 'pedrorodrigues');
INSERT INTO user_assinatura VALUES('77073371234', 'ALFREDO JOSE CARNEIRO DA SILVA', 'ANALISTA DE SUPORTE V', 'Mônaco Motocenter', NULL, '91981352813', 'ALFREDO');
INSERT INTO user_assinatura VALUES('00086612271', 'SILVIO CARLOS MOTA SANTOS', 'ADMINISTRADOR DE REDE', 'Mônaco Participações', '9130755705', '91991047665', 'SILVIOMOTA');
INSERT INTO user_assinatura VALUES('02644270251', 'LUCAS PANTOJA CARDOSO', 'ANALISTA DE SUPORTE', 'Mônaco Participações', NULL, '91993525462', 'lucascardoso');
INSERT INTO user_assinatura VALUES('05318373194', 'GIOVANNI LOPES DE CARVALHO', 'ASSISTENTE TI', 'Mônaco Fiat', NULL, '66997172330', 'giovanni.mt');
INSERT INTO user_assinatura VALUES('57742596253', 'ULISSES DIAS DE ARAUJO', 'ANALISTA DE TI', 'Mônaco Veículos', '9131811049', '91931811049', 'ulisses.fiat');


SELECT * FROM user_assinatura 
                            WHERE email_user = 'PEDRORODRIGUES';



COMMIT WORK;
