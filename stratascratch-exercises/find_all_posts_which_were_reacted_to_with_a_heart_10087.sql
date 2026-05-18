select * from facebook_posts p
where p.post_id IN
(
    select
        r.post_id
    from facebook_reactions r
    where r.reaction = 'heart'
);
