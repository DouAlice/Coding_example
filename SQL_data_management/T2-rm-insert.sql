

-- =======================================
-- EMERCONTACT
-- =======================================
INSERT INTO emercontact (
    ec_phone,
    ec_fname,
    ec_lname
) VALUES (
    '0400123123',
    'Nina',
    'Zeng'
);

INSERT INTO emercontact (
    ec_phone,
    ec_fname,
    ec_lname
) VALUES (
    '0400123001',
    'Vic',
    'Jones'
);

INSERT INTO emercontact (
    ec_phone,
    ec_fname,
    ec_lname
) VALUES (
    '0400123002',
    'Crystal',
    'Clarke'
);

INSERT INTO emercontact (
    ec_phone,
    ec_fname,
    ec_lname
) VALUES (
    '0400123003',
    'Amy',
    'Tran'
);

INSERT INTO emercontact (
    ec_phone,
    ec_fname,
    ec_lname
) VALUES (
    '0400123125',
    'Egan',
    'Putuyu'
);

-- =======================================
-- COMPETITOR
-- =======================================

INSERT INTO competitor VALUES (
    10001,
    'Evan',
    'Tran',
    'M',
    TO_DATE(' 07/07/2006', 'dd/mm/yyyy'),
    'evan.t@gmail.com',
    'N',
    '0499100001',
    'P',
    '0400123003'
);

INSERT INTO competitor VALUES (
    10002,
    'Elane',
    'Tran',
    'F',
    TO_DATE(' 10/11/2007', 'dd/mm/yyyy'),
    'elane.t@gmail.com',
    'N',
    '0499100002',
    'P',
    '0400123003'
);

INSERT INTO competitor VALUES (
    10003,
    'Steve',
    'Tsu',
    'M',
    TO_DATE(' 07/01/1998', 'dd/mm/yyyy'),
    'steve.tsu@gmail.com',
    'Y',
    '0499100003',
    'F',
    '0400123123'
);

INSERT INTO competitor VALUES (
    10004,
    'Shane',
    'Hogan',
    'F',
    TO_DATE(' 22/05/1994', 'dd/mm/yyyy'),
    'shane.h@gmail.com',
    'Y',
    '0499100004',
    'T',
    '0400123125'
);

INSERT INTO competitor VALUES (
    10005,
    'Dan',
    'Little',
    'M',
    TO_DATE(' 04/08/1988', 'dd/mm/yyyy'),
    'dan.l@gmail.com',
    'Y',
    '0499100005',
    'F',
    '0400123123'
);

INSERT INTO competitor VALUES (
    10006,
    'Sui',
    'Qin',
    'U',
    TO_DATE(' 09/11/1996', 'dd/mm/yyyy'),
    'sui.q@gmail.com',
    'Y',
    '0499100006',
    'F',
    '0400123125'
);

INSERT INTO competitor VALUES (
    10007,
    'Niko',
    'Tsumaru',
    'F',
    TO_DATE(' 03/06/1995', 'dd/mm/yyyy'),
    'niko.t@gmail.com',
    'Y',
    '0499100007',
    'T',
    '0400123125'
);

INSERT INTO competitor VALUES (
    10008,
    'Shirin',
    'Maghool',
    'F',
    TO_DATE(' 12/08/1993', 'dd/mm/yyyy'),
    'shirin.m@gmail.com',
    'Y',
    '0499100008',
    'F',
    '0400123001'
);

INSERT INTO competitor VALUES (
    10009,
    'Paul',
    'Citron',
    'M',
    TO_DATE(' 01/03/1994', 'dd/mm/yyyy'),
    'paul.c@gmail.com',
    'Y',
    '0499100009',
    'F',
    '0400123002'
);

INSERT INTO competitor VALUES (
    10010,
    'Lindsay',
    'Smith',
    'M',
    TO_DATE(' 13/12/1956', 'dd/mm/yyyy'),
    'lindsay.s@gmail.com',
    'Y',
    '0499100010',
    'F',
    '0400123002'
);

INSERT INTO competitor VALUES (
    10011,
    'Cat',
    'More',
    'U',
    TO_DATE(' 01/12/2000', 'dd/mm/yyyy'),
    'cat.m@gmail.com',
    'Y',
    '0499100011',
    'F',
    '0400123002'
);

INSERT INTO competitor VALUES (
    10012,
    'Abby',
    'Hong',
    'U',
    TO_DATE(' 01/05/1999', 'dd/mm/yyyy'),
    'abby.h@gmail.com',
    'Y',
    '0499100012',
    'F',
    '0400123123'
);

INSERT INTO competitor VALUES (
    10013,
    'Adi',
    'Hong',
    'U',
    TO_DATE(' 01/05/1999', 'dd/mm/yyyy'),
    'adi.h@gmail.com',
    'Y',
    '0499100013',
    'F',
    '0400123123'
);

INSERT INTO competitor VALUES (
    10014,
    'Acne',
    'Hong',
    'U',
    TO_DATE(' 01/05/1999', 'dd/mm/yyyy'),
    'acne.h@gmail.com',
    'Y',
    '0499100014',
    'F',
    '0400123123'
);

INSERT INTO competitor VALUES (
    10015,
    'Amory',
    'Hong',
    'U',
    TO_DATE(' 01/05/1999', 'dd/mm/yyyy'),
    'amory.h@gmail.com',
    'Y',
    '0499100015',
    'F',
    '0400123123'
);

-- =======================================
-- ENTRY
-- =======================================

INSERT INTO entry VALUES (
    14,
    30001,
    TO_DATE('08:00:25', 'HH:MI:SS'),
    TO_DATE('08:30:58', 'HH:MI:SS'),
    10001,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    2,
    30002,
    TO_DATE('08:30:03', 'HH:MI:SS'),
    NULL,
    10001,
    NULL,
    2
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    14,
    30003,
    NULL,
    NULL,
    10002,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    6,
    30004,
    TO_DATE('08:30:05', 'HH:MI:SS'),
    TO_DATE('09:45:00', 'HH:MI:SS'),
    10002,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    10,
    30005,
    TO_DATE('08:00:08', 'HH:MI:SS'),
    TO_DATE('08:25:48', 'HH:MI:SS'),
    10002,
    NULL,
    3
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    10,
    30006,
    TO_DATE('08:37:03', 'HH:MI:SS'),
    TO_DATE('09:45:58', 'HH:MI:SS'),
    10003,
    NULL,
    2
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    7,
    30007,
    TO_DATE('08:33:54', 'HH:MI:SS'),
    TO_DATE('08:55:12', 'HH:MI:SS'),
    10003,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    8,
    30008,
    TO_DATE('08:05:00', 'HH:MI:SS'),
    TO_DATE('08:55:01', 'HH:MI:SS'),
    10004,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    11,
    30009,
    TO_DATE('07:53:01', 'HH:MI:SS'),
    TO_DATE('08:59:00', 'HH:MI:SS'),
    10004,
    NULL,
    2
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    12,
    30010,
    NULL,
    NULL,
    10005,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    7,
    30011,
    NULL,
    NULL,
    10006,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    3,
    30012,
    TO_DATE('09:00:07', 'HH:MI:SS'),
    NULL,
    10006,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    3,
    30013,
    TO_DATE('08:32:31', 'HH:MI:SS'),
    TO_DATE('09:54:04', 'HH:MI:SS'),
    10007,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    8,
    30014,
    TO_DATE('08:01:00', 'HH:MI:SS'),
    TO_DATE('08:58:46', 'HH:MI:SS'),
    10007,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    11,
    30015,
    NULL,
    NULL,
    10007,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    13,
    30016,
    NULL,
    NULL,
    10007,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    2,
    30017,
    TO_DATE('08:30:05', 'HH:MI:SS'),
    TO_DATE('09:09:00', 'HH:MI:SS'),
    10008,
    NULL,
    2
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    5,
    30018,
    TO_DATE('08:00:07', 'HH:MI:SS'),
    TO_DATE('09:35:00', 'HH:MI:SS'),
    10008,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    6,
    30019,
    TO_DATE('08:30:01', 'HH:MI:SS'),
    TO_DATE('08:39:05', 'HH:MI:SS'),
    10008,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    13,
    30020,
    NULL,
    NULL,
    10008,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    14,
    30021,
    NULL,
    NULL,
    10009,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    10,
    30022,
    TO_DATE('08:00:15', 'HH:MI:SS'),
    TO_DATE('08:15:00', 'HH:MI:SS'),
    10009,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    3,
    30023,
    TO_DATE('09:00:13', 'HH:MI:SS'),
    NULL,
    10009,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    1,
    30024,
    TO_DATE('09:30:08', 'HH:MI:SS'),
    TO_DATE('09:47:02', 'HH:MI:SS'),
    10009,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    1,
    30025,
    TO_DATE('09:31:00', 'HH:MI:SS'),
    TO_DATE('10:02:05', 'HH:MI:SS'),
    10010,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    3,
    30026,
    TO_DATE('09:05:00', 'HH:MI:SS'),
    NULL,
    10010,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    10,
    30027,
    TO_DATE('08:00:01', 'HH:MI:SS'),
    TO_DATE('08:15:05', 'HH:MI:SS'),
    10010,
    NULL,
    NULL
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    14,
    30028,
    NULL,
    NULL,
    10010,
    NULL,
    4
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    6,
    30029,
    TO_DATE('08:31:00', 'HH:MI:SS'),
    TO_DATE('09:58:01', 'HH:MI:SS'),
    10011,
    NULL,
    1
);

INSERT INTO entry (
    event_id,
    entry_no,
    entry_starttime,
    entry_finishtime,
    comp_no,
    team_id,
    char_id
) VALUES (
    10,
    30030,
    TO_DATE('08:00:59', 'HH:MI:SS'),
    TO_DATE('08:36:59', 'HH:MI:SS'),
    10011,
    NULL,
    1
);

-- =======================================
-- TEAM
-- =======================================

INSERT INTO team (
    team_id,
    team_name,
    carn_date,
    team_no_members,
    event_id,
    entry_no,
    char_id
) VALUES (
    10,
    'Number one',
    TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),
    2,
    1,
    30025,
    1
);

INSERT INTO team VALUES (
    11,
    'Number one',
    TO_DATE('05/FEB/2022', 'DD/MON/YYYY'),
    3,
    6,
    30029,
    1
);

INSERT INTO team VALUES (
    12,
    'Lonely fighter',
    TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),
    1,
    5,
    30018,
    1
);

INSERT INTO team VALUES (
    13,
    'Best couple',
    TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),
    2,
    2,
    30002,
    2
);

INSERT INTO team VALUES (
    14,
    'Born to win',
    TO_DATE('29/May/2022', 'DD/MON/YYYY'),
    1,
    12,
    30010,
    4
);

UPDATE entry
SET
    team_id = 13
WHERE
        event_id = 14
    AND entry_no = 30001;

UPDATE entry
SET
    team_id = 11
WHERE
        event_id = 6
    AND entry_no = 30004;

UPDATE entry
SET
    team_id = 14
WHERE
        event_id = 12
    AND entry_no = 30010;

UPDATE entry
SET
    team_id = 13
WHERE
        event_id = 2
    AND entry_no = 30017;

UPDATE entry
SET
    team_id = 12
WHERE
        event_id = 5
    AND entry_no = 30018;

UPDATE entry
SET
    team_id = 11
WHERE
        event_id = 6
    AND entry_no = 30019;

UPDATE entry
SET
    team_id = 10
WHERE
        event_id = 1
    AND entry_no = 30024;

UPDATE entry
SET
    team_id = 10
WHERE
        event_id = 1
    AND entry_no = 30025;

UPDATE entry
SET
    team_id = 11
WHERE
        event_id = 6
    AND entry_no = 30029;

COMMIT;