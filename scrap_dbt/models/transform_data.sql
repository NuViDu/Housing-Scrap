with final as (
    select
        housing.id,
        price,
        size,
        housing_type,
        regexp_replace(regexp_replace(regexp_replace(regexp_replace(address, 'ö', 'oe'), 'ä', 'ae'), 'ü', 'ue'), 'ß', 'ss') as "address",
        trim(housing_type) as "housing_type",
        provider_type,
        rent_price_info,
        listing_day,
        listing_month,
        listing_year,
        add_date.listing_date
    from housing join add_date
    on housing.id = add_date.id
)
select * from final