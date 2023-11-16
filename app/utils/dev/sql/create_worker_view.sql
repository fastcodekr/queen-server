# # subquery
drop table if exists worker_view;
drop view if exists worker_view;
create view worker_view as
select workers.id                                                                                                                   as id,
       workers.created_at                                                                                                           as created_at,
       workers.updated_at                                                                                                           as updated_at,
       (select farms.location_id
        from farms
        where farms.id = (select contracts.farm_id
                          from contracts
                          where contracts.worker_id = workers.id))                                                                  as location_id,
       (select locations.name
        from locations
        where locations.id = (select farms.location_id
                              from farms
                              where farms.id = (select contracts.farm_id
                                                from contracts
                                                where contracts.worker_id = workers.id)))                                           as location_name,
       (select contracts.farm_id
        from contracts
        where contracts.worker_id = workers.id)                                                                                     as farm_id,
       (select farms.name
        from farms
        where farms.id = (select contracts.farm_id
                          from contracts
                          where contracts.worker_id = workers.id))                                                                  as farm_name,
       workers.team_id                                                                                                              as team_id,
       (select teams.name from teams where teams.id = workers.team_id)                                                              as team_name,
       (select people.first_name
        from people
        where people.id = workers.person_id)                                                                                        as first_name,
       (select people.last_name
        from people
        where people.id = workers.person_id)                                                                                        as last_name,
       (select people.english_name
        from people
        where people.id = workers.person_id)                                                                                        as english_name,
       (select bank_details.bsb
        from bank_details
        where bank_details.personal_detail_id = (select personal_details.id
                                                 from personal_details
                                                 where personal_details.contract_id = (select contracts.id
                                                                                       from contracts
                                                                                       where contracts.worker_id = workers.id)))    as bsb,
       (select bank_details.account_number
        from bank_details
        where bank_details.personal_detail_id = (select personal_details.id
                                                 from personal_details
                                                 where personal_details.contract_id = (select contracts.id
                                                                                       from contracts
                                                                                       where contracts.worker_id = workers.id)))    as account_number,
       (select personal_details.email
        from personal_details
        where personal_details.contract_id = (select contracts.id
                                              from contracts
                                              where contracts.worker_id = workers.id))                                              as email,
       (select personal_details.cell_phone
        from personal_details
        where personal_details.contract_id = (select contracts.id
                                              from contracts
                                              where contracts.worker_id = workers.id))                                              as cell_phone,
       (select personal_details.tax_file_number
        from personal_details
        where personal_details.contract_id = (select contracts.id
                                              from contracts
                                              where contracts.worker_id = workers.id))                                              as tax_file_number,
       (select people.birth_date
        from people
        where people.id = workers.person_id)                                                                                        as birth_date,
       (select people.gender
        from people
        where people.id = workers.person_id)                                                                                        as gender,
       (select passports.nationality
        from passports
        where passports.person_id = workers.person_id)                                                                              as nationality,
       (select passports.passport_number
        from passports
        where passports.person_id = workers.person_id)                                                                              as passport_number,
       (select passports.visa_grant_number
        from passports
        where passports.person_id = workers.person_id)                                                                              as visa_grant_number,
       (select superannuations.fund_name
        from superannuations
        where superannuations.personal_detail_id = (select personal_details.id
                                                    from personal_details
                                                    where personal_details.contract_id = (select contracts.id
                                                                                          from contracts
                                                                                          where contracts.worker_id = workers.id))) as fund_name,
       (select superannuations.member_number
        from superannuations
        where superannuations.personal_detail_id = (select personal_details.id
                                                    from personal_details
                                                    where personal_details.contract_id = (select contracts.id
                                                                                          from contracts
                                                                                          where contracts.worker_id = workers.id))) as member_number,
       (select personal_details.address
        from personal_details
        where personal_details.contract_id = (select contracts.id
                                              from contracts
                                              where contracts.worker_id = workers.id))                                              as address,
       workers.start_date                                                                                                           as start_date,
       workers.end_date                                                                                                             as end_date,
       workers.tax                                                                                                                  as tax,
       workers.farm_number                                                                                                          as farm_number,
       workers.memo                                                                                                                 as memo
from workers
;

# # join
# drop table if exists worker_view;
# drop view if exists worker_view;
# create view worker_view as
# select workers.id                       as id,
#        workers.created_at               as created_at,
#        workers.updated_at               as updated_at,
#        farms.location_id                as location_id,
#        locations.name                   as location_name,
#        contracts.farm_id                as farm_id,
#        farms.name                       as farm_name,
#        workers.team_id                  as team_id,
#        teams.name                       as team_name,
#        people.first_name                as first_name,
#        people.last_name                 as last_name,
#        people.english_name              as english_name,
#        bank_details.bsb                 as bsb,
#        bank_details.account_number      as account_number,
#        personal_details.email           as email,
#        personal_details.cell_phone      as cell_phone,
#        personal_details.tax_file_number as tax_file_number,
#        people.birth_date                as birth_date,
#        people.gender                    as gender,
#        passports.nationality            as nationality,
#        passports.passport_number        as passport_number,
#        passports.visa_grant_number      as visa_grant_number,
#        superannuations.fund_name        as fund_name,
#        superannuations.member_number    as member_number,
#        personal_details.address         as address,
#        workers.start_date               as start_date,
#        workers.end_date                 as end_date,
#        workers.tax                      as tax,
#        workers.farm_number              as farm_number,
#        workers.memo                     as memo
# from workers
#          left join contracts on workers.id = contracts.worker_id
#          left join farms on contracts.farm_id = farms.id
#          left join locations on farms.location_id = locations.id
#          left join teams on workers.team_id = teams.id
#          left join people on workers.person_id = people.id
#          left join personal_details on contracts.id = personal_details.contract_id
#          left join bank_details on personal_details.id = bank_details.personal_detail_id
#          left join passports on people.id = passports.person_id
#          left join superannuations on personal_details.id = superannuations.personal_detail_id
# ;