with months as (
    select to_char(a.shipment_date, 'YYYY-MM') as month
    from amazon_shipment a
)

select month, count(*) from months
group by month
