DROP TABLE if exists weapon;
DROP TABLE if exists sub;
create table if not exists sub (
    sub_id smallint,
    sub_name varchar(50),
    primary key(sub_id)
);

create table if not exists special (
    special_id smallint,
    special_name varchar(50),
    primary key(special_id)
);

create table if not exists weapon (
    weapon_id smallint,
    weapon_name varchar(50),
    sub_id smallint,
    range_distance smallint,
    types varchar(50),
    primary key(weapon_id),
    foreign key (sub_id) references sub(sub_id)
);

create table if not exists test (
    weapon_id smallint,
    weapon_name varchar(50),
    sub_id smallint,
    range_distance smallint,
    types varchar(50),
    primary key(weapon_id),
    foreign key (sub_id) references sub(sub_id)
);