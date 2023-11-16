insert into people(id, first_name, last_name, english_name, gender, birth_date)
values (1, 'Ryota', 'Nishikawa', null, 'male', '1999-10-22');
insert into people(id, first_name, last_name, english_name, gender, birth_date)
values (2, 'Anri', 'Tsukui', null, 'female', '1998-09-14');
insert into people(id, first_name, last_name, english_name, gender, birth_date)
values (3, 'Minjoo', 'Yu', 'Celina', 'female', '1998-05-29');

insert into passports(person_id, id, nationality, passport_number, visa_grant_number)
values (1, 1, 'Japan', 'TT1716205', '2009503263977');
insert into passports(person_id, id, nationality, passport_number, visa_grant_number)
values (2, 2, 'Japan', 'TS3751904', '2009584532071');
insert into passports(person_id, id, nationality, passport_number, visa_grant_number)
values (3, 3, 'Korea', 'M15331550', '2009579935397');

insert into workers(person_id, id, tax, farm_number)
values (1, 1, '90', '26076');
insert into workers(person_id, id, tax, farm_number)
values (2, 2, '85', '26110');
insert into workers(person_id, id, tax, farm_number)
values (3, 3, '90', '26089');

insert into contracts(farm_id, worker_id, id)
values (1, 1, 1);
insert into contracts(farm_id, worker_id, id)
values (2, 2, 2);
insert into contracts(farm_id, worker_id, id)
values (3, 3, 3);

insert into personal_details(contract_id, id, cell_phone, email, address, tax_file_number)
values (1, 1, '0483 326 513', 'sggk.r.no.1@gmail.com', '27 Mortimer Caboolture QLD 4510', '443 582 531');
insert into personal_details(contract_id, id, cell_phone, email, address, tax_file_number)
values (2, 2, '0420 481 409', 'anri291t@icloud.com', '27 Mortimer Caboolture QLD 4510', '446 656 740');
insert into personal_details(contract_id, id, cell_phone, email, address, tax_file_number)
values (3, 3, '0491 173 873', 'mju0529@gmail.com', '4 longman st caboolture south QLD 4510', '584 626 459');

insert into superannuations(personal_detail_id, id, fund_name, member_number)
values (1, 1, null, '903328665');
insert into superannuations(personal_detail_id, id, fund_name, member_number)
values (2, 2, 'Rest Super', '713973398');
insert into superannuations(personal_detail_id, id, fund_name, member_number)
values (3, 3, null, null);

insert into bank_details(personal_detail_id, id, bsb, account_number)
values (1, 1, '013 128', '432912572');
insert into bank_details(personal_detail_id, id, bsb, account_number)
values (2, 2, '084 745', '205529354');
insert into bank_details(personal_detail_id, id, bsb, account_number)
values (3, 3, '063 097', '77069694');