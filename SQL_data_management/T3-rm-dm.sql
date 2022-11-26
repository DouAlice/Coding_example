
--3(a)
DROP SEQUENCE comp_no_seq;

CREATE SEQUENCE comp_no_seq START WITH 100 INCREMENT BY 1;

DROP SEQUENCE team_id_seq;

CREATE SEQUENCE team_id_seq START WITH 100 INCREMENT BY 1;

--3(b)

INSERT INTO emercontact VALUES (
    '0476541234',
    'Jack',
    'Kai'
);

INSERT INTO competitor VALUES (
    comp_no_seq.NEXTVAL,
    'Daniel',
    'Kai',
    'M',
    TO_DATE('01/01/2001', 'dd/mm/yyyy'),
    'daniel.k@gmail.com',
    'Y',
    '0476000001',
    'P',
    '0476541234'
);

INSERT INTO entry VALUES (
    (
        SELECT
            e.event_id
        FROM
                 carnival c
            JOIN event     e ON c.carn_date = e.carn_date
            JOIN eventtype t ON t.eventtype_code = e.eventtype_code
        WHERE
                carn_name = 'RM Autumn Series Caulfield 2022'
            AND eventtype_desc = '21.1 Km Half Marathon'
    ),
    31001,
    NULL,
    NULL,
    comp_no_seq.CURRVAL,
    NULL,
    (
        SELECT
            char_id
        FROM
            charity
        WHERE
            char_name = 'Beyond Blue'
    )
);

INSERT INTO competitor (
    comp_no,
    comp_fname,
    comp_lname,
    comp_gender,
    comp_dob,
    comp_email,
    comp_unistatus,
    comp_phone,
    comp_ec_relationship,
    ec_phone
) VALUES (
    comp_no_seq.NEXTVAL,
    'Annabelle',
    'Kai',
    'F',
    TO_DATE(' 10/3/2002', 'dd/mm/yyyy'),
    'annabelle.k@gmail.com',
    'Y',
    '0476000002',
    'P',
    '0476541234'
);

INSERT INTO entry VALUES (
    (
        SELECT
            e.event_id
        FROM
                 carnival c
            JOIN event     e ON c.carn_date = e.carn_date
            JOIN eventtype t ON t.eventtype_code = e.eventtype_code
        WHERE
                carn_name = 'RM Autumn Series Caulfield 2022'
            AND eventtype_desc = '21.1 Km Half Marathon'
    ),
    31002,
    NULL,
    NULL,
    comp_no_seq.CURRVAL,
    NULL,
    (
        SELECT
            char_id
        FROM
            charity
        WHERE
            char_name = 'Amnesty International'
    )
);

COMMIT;

--3(c)

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    event_id,
    entry_no,
    char_id
) VALUES (
    team_id_seq.NEXTVAL,
    'Kai Speedstars',
    (
        SELECT
            carn_date
        FROM
            carnival
        WHERE
            carn_name = 'RM Autumn Series Caulfield 2022'
    ),
    1,
    (
        SELECT
            event_id
        FROM
                 carnival c
            JOIN event     e ON c.carn_date = e.carn_date
            JOIN eventtype t ON t.eventtype_code = e.eventtype_code
        WHERE
                carn_name = 'RM Autumn Series Caulfield 2022'
            AND eventtype_desc = '21.1 Km Half Marathon'
    ),
    (
        SELECT
            entry_no
        FROM
                 carnival c
            JOIN event      e ON c.carn_date = e.carn_date
            JOIN entry      t ON e.event_id = t.event_id
            JOIN competitor cm ON cm.comp_no = t.comp_no
        WHERE
                comp_fname = 'Annabelle'
            AND comp_lname = 'Kai'
            AND carn_name = 'RM Autumn Series Caulfield 2022'
    ),
    (
        SELECT
            char_id
        FROM
            charity
        WHERE
            char_name = 'Beyond Blue'
    )
);

UPDATE entry
SET
    team_id = team_id_seq.CURRVAL
WHERE
        entry_no = (
            SELECT
                entry_no
            FROM
                     carnival c
                JOIN event      e ON c.carn_date = e.carn_date
                JOIN entry      t ON e.event_id = t.event_id
                JOIN competitor cm ON cm.comp_no = t.comp_no
            WHERE
                    cm.comp_fname = 'Annabelle'
                AND cm.comp_lname = 'Kai'
                AND c.carn_name = 'RM Autumn Series Caulfield 2022'
        )
    AND event_id = (
        SELECT
            event_id
        FROM
                 carnival c
            JOIN event     e ON c.carn_date = e.carn_date
            JOIN eventtype t ON t.eventtype_code = e.eventtype_code
        WHERE
                carn_name = 'RM Autumn Series Caulfield 2022'
            AND eventtype_desc = '21.1 Km Half Marathon'
    );

COMMIT;
  

    

--3(d)

UPDATE entry
SET
    event_id = (
        SELECT
            event_id
        FROM
                 event n
            JOIN eventtype t ON n.eventtype_code = t.eventtype_code
        WHERE
                eventtype_desc = '10 Km Run'
            AND carn_date = (
                SELECT
                    carn_date
                FROM
                    carnival
                WHERE
                    carn_name = 'RM Autumn Series Caulfield 2022'
            )
    ),
    team_id = (
        SELECT
            team_id
        FROM
            team
        WHERE
                team_name = 'Kai Speedstars'
            AND carn_date = (
                SELECT
                    carn_date
                FROM
                    carnival
                WHERE
                    carn_name = 'RM Autumn Series Caulfield 2022'
            )
    )
WHERE
        entry_no = (
            SELECT
                entry_no
            FROM
                     carnival c
                JOIN event      e ON c.carn_date = e.carn_date
                JOIN entry      t ON e.event_id = t.event_id
                JOIN competitor cm ON cm.comp_no = t.comp_no
            WHERE
                    comp_fname = 'Daniel'
                AND comp_lname = 'Kai'
                AND carn_name = 'RM Autumn Series Caulfield 2022'
        )
    AND event_id = (
        SELECT
            event_id
        FROM
                 event n
            JOIN eventtype t ON n.eventtype_code = t.eventtype_code
        WHERE
                eventtype_desc = '21.1 Km Half Marathon'
            AND carn_date = (
                SELECT
                    carn_date
                FROM
                    carnival
                WHERE
                    carn_name = 'RM Autumn Series Caulfield 2022'
            )
    );

UPDATE team
SET
    team_no_members = ( team_no_members + 1 )
WHERE
        team_name = 'Kai Speedstars'
    AND carn_date = (
        SELECT
            carn_date
        FROM
            carnival
        WHERE
            carn_name = 'RM Autumn Series Caulfield 2022'
    );

COMMIT;

--3(e)

DELETE FROM entry
WHERE
    entry_no = (
        SELECT
            entry_no
        FROM
                 carnival c
            JOIN event      e ON c.carn_date = e.carn_date
            JOIN entry      t ON e.event_id = t.event_id
            JOIN competitor cm ON cm.comp_no = t.comp_no
        WHERE
                comp_fname = 'Daniel'
            AND comp_lname = 'Kai'
            AND carn_name = 'RM Autumn Series Caulfield 2022'
    );

UPDATE entry
SET
    char_id = (
        SELECT
            char_id
        FROM
            charity
        WHERE
            char_name = 'Beyond Blue'
    ),
    team_id = NULL
WHERE
    entry_no = (
        SELECT
            entry_no
        FROM
                 carnival c
            JOIN event      e ON c.carn_date = e.carn_date
            JOIN entry      t ON e.event_id = t.event_id
            JOIN competitor cm ON cm.comp_no = t.comp_no
        WHERE
                cm.comp_fname = 'Annabelle'
            AND cm.comp_lname = 'Kai'
            AND c.carn_name = 'RM Autumn Series Caulfield 2022'
    );

DELETE FROM team
WHERE
        team_name = 'Kai Speedstars'
    AND carn_date = (
        SELECT
            carn_date
        FROM
            carnival
        WHERE
            carn_name = 'RM Autumn Series Caulfield 2022'
    );

COMMIT;