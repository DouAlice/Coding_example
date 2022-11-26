

DROP TABLE official;

DROP TABLE role;

DROP TABLE team_charity;

--4(a)
ALTER TABLE entry ADD entry_elapsed_time NUMERIC(5, 2);

UPDATE entry
SET
    entry_elapsed_time = round((entry_finishtime - entry_starttime) * 24 * 60, 2);

COMMENT ON COLUMN entry.entry_elapsed_time IS
    'The runner’s elapsed time in an event stored as the number of minutes elapsed to two decimal places eg. 26.82';

COMMIT;


--4(b)

CREATE TABLE team_charity (
    team_id              NUMERIC(3) NOT NULL,
    char_id              NUMBER(3) NOT NULL,
    team_fund_percentage NUMERIC(3)
);

COMMENT ON COLUMN team_charity.team_id IS
    'Team identifier (unique)';

COMMENT ON COLUMN team_charity.char_id IS
    'Charity id (unique identifier for charity)';

COMMENT ON COLUMN team_charity.team_fund_percentage IS
    'the percentage (0 to 100) of total raised funds that goes to each charity';

ALTER TABLE team_charity ADD CONSTRAINT team_charity_pk PRIMARY KEY ( team_id,
                                                                      char_id );

ALTER TABLE team_charity
    ADD CONSTRAINT team_charity_team_fk FOREIGN KEY ( team_id )
        REFERENCES team ( team_id );

ALTER TABLE team_charity
    ADD CONSTRAINT team_charity_charity_fk FOREIGN KEY ( char_id )
        REFERENCES charity ( char_id );

ALTER TABLE team_charity
    ADD CONSTRAINT team_fund_percentage_chk CHECK ( team_fund_percentage > 0
                                                    AND team_fund_percentage <= 100 );

  
  
  
        
--4(c)

CREATE TABLE role (
    role_id   NUMERIC(5) NOT NULL,
    role_name VARCHAR2(20) NOT NULL
);

COMMENT ON COLUMN role.role_id IS
    'a unique number created to identify each role an offical can take';

COMMENT ON COLUMN role.role_name IS
    'the name of the official’s role';

ALTER TABLE role ADD CONSTRAINT role_pk PRIMARY KEY ( role_id );

DROP SEQUENCE role_id_seq;

CREATE SEQUENCE role_id_seq START WITH 1 INCREMENT BY 1;

INSERT INTO role VALUES (
    role_id_seq.NEXTVAL,
    'time keeper'
);

INSERT INTO role VALUES (
    role_id_seq.NEXTVAL,
    'marshal'
);

INSERT INTO role VALUES (
    role_id_seq.NEXTVAL,
    'starter'
);

INSERT INTO role VALUES (
    role_id_seq.NEXTVAL,
    'first aid'
);

COMMIT;

CREATE TABLE official (
    carn_date DATE NOT NULL,
    comp_no   NUMERIC(5) NOT NULL,
    role_id   NUMERIC(5) NOT NULL
);

COMMENT ON COLUMN official.carn_date IS
    'Date of carnival (a unique identifier of carnival)';

COMMENT ON COLUMN official.comp_no IS
    'Unique identifier for a competitor';

COMMENT ON COLUMN official.role_id IS
    'a unique number to identify each role an offical takes';

ALTER TABLE official ADD CONSTRAINT official_pk PRIMARY KEY ( carn_date,
                                                              comp_no );

ALTER TABLE official
    ADD CONSTRAINT official_carnival_fk FOREIGN KEY ( carn_date )
        REFERENCES carnival ( carn_date );

ALTER TABLE official
    ADD CONSTRAINT official_competitor_fk FOREIGN KEY ( comp_no )
        REFERENCES competitor ( comp_no );

ALTER TABLE official
    ADD CONSTRAINT official_role_fk FOREIGN KEY ( role_id )
        REFERENCES role ( role_id );
        
select * from competitor;
select * from team;
select * from entry;
select * from competitor;