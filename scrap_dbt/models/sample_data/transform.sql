with final as (
    select 
        replace(replace(replace(replace("Address", 'ß', 'ss'), 'ö', 'oe'), 'ü', 'ue'), 'ä', 'ae') as "Address",
        trim("Housing Type") as "Housing Type"
    from {{ref('Berlin_housing_data')}}
)

select * from final