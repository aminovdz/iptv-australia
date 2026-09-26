import { defineCollection, z } from 'astro:content';

const guidesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('AU IPTV Tech Team'),
    image: z.string().default('/images/og-banner.webp'),
    imageAlt: z.string().default('AU IPTV Australia Streaming Guide & Setup'),
    tags: z.array(z.string()).default(['AU IPTV', 'IPTV Australia', 'Streaming Setup', 'NBN Compatibility']),
    featured: z.boolean().default(false),
    readingTime: z.string().default('5 min read'),
    category: z.string().default('Guides & Tutorials'),
    targetKeyword: z.string().optional()
  })
});

export const collections = {
  guides: guidesCollection
};
