import streamlit as st
import datetime

# 设置页面配置
st.set_page_config(
    page_title="Do I Dare Disturb - Measured Silence",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式 - 2013年博客风格
st.markdown("""
<style>
    /* 2013年博客风格CSS */
    .main {
        background-color: #f8f8f8;
        font-family: 'Georgia', serif;
    }
    
    .stApp {
        background-color: #f8f8f8;
    }
    
    .blog-header {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 3rem;
        border-radius: 12px;
        margin-bottom: 3rem;
        text-align: center;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .blog-title {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .blog-subtitle {
        font-size: 1.4rem;
        font-style: italic;
        opacity: 0.9;
        line-height: 1.6;
    }
    
    .author-info {
        background-color: white;
        padding: 2.5rem;
        border-radius: 12px;
        margin: 2rem 0;
        border-left: 6px solid #3498db;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        line-height: 1.8;
    }
    
    .blog-post {
        background-color: white;
        padding: 3rem;
        border-radius: 12px;
        margin: 2.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-top: 4px solid #e74c3c;
        line-height: 1.8;
    }
    
    .post-title {
        color: #2c3e50;
        font-size: 2.2rem;
        font-weight: bold;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .post-meta {
        color: #7f8c8d;
        font-size: 1rem;
        margin-bottom: 2rem;
        font-style: italic;
        padding-bottom: 1rem;
        border-bottom: 1px solid #ecf0f1;
    }
    
    .post-content {
        line-height: 2.0;
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    .post-content p {
        margin-bottom: 1.5rem;
    }
    
    .post-content h3 {
        color: #34495e;
        margin: 2rem 0 1rem 0;
        font-size: 1.5rem;
    }
    
    .post-content ul {
        margin: 1.5rem 0;
        padding-left: 2rem;
    }
    
    .post-content li {
        margin-bottom: 0.8rem;
    }
    
    .sidebar-content {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .tag {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 0.3rem;
        text-decoration: none;
    }
    
    .quote {
        border-left: 5px solid #e74c3c;
        padding: 1.5rem;
        margin: 2rem 0;
        font-style: italic;
        color: #7f8c8d;
        background-color: #f8f9fa;
        border-radius: 0 8px 8px 0;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, #3498db, #e74c3c);
        margin: 3rem 0;
        border-radius: 1px;
    }
</style>
""", unsafe_allow_html=True)

# 博客数据
blog_posts = [
    {
        "title": "The Whisperers: Voices from the Digital Shadows (2000-2005)",
        "date": "2013-12-15",
        "tags": ["Silent Voices", "Digital Memory", "Human Stories", "Forgotten Histories"],
        "content": """
        <div class="post-content">
        <p>Sometimes I think about the early days of the internet, not as a technological revolution, but as a gathering place for voices that had nowhere else to go. In those first years of the new millennium, before social media became what it is today, there were corners of the web where people spoke in whispers, sharing stories that would otherwise be lost to silence.</p>
        
        <div class="quote">
        "Every silence has a story. Every story has a voice that deserves to be heard, even if only once." - Anonymous, 2001
        </div>
        
        <p>I remember reading through old forum posts from 2001-2003, archived in the depths of university servers. These weren't the grand narratives of political change or technological advancement. They were the small, personal stories of people documenting their daily lives in a world that was rapidly changing around them. A mother in Tehran posting about her son's first steps, just as the first signs of digital surveillance were appearing. A student in Beijing sharing poetry that would later be censored. A librarian in a small American town documenting the gradual disappearance of physical books.</p>
        
        <h3>Fragments of Memory:</h3>
        <ul>
        <li><strong>2001:</strong> The first personal blogs appeared, often written by people who had never had a public voice before</li>
        <li><strong>2002:</strong> Online communities formed around shared experiences of loss and hope</li>
        <li><strong>2003:</strong> The first cases of digital content being "disappeared" by governments</li>
        <li><strong>2004:</strong> Citizen journalists began documenting events that mainstream media ignored</li>
        <li><strong>2005:</strong> The emergence of digital archives preserving voices that would otherwise be lost</li>
        </ul>
        
        <p>These weren't the stories that made headlines. They were the quiet observations of ordinary people trying to make sense of a world that was becoming both more connected and more isolated. In my work at the library, I often think about how we preserve these digital whispers. Each one is a piece of someone's truth, a fragment of human experience that deserves to be remembered.</p>
        
        <p>Perhaps that's why I find myself drawn to these early digital spaces. They remind me that behind every technological advancement, there are human stories waiting to be told. Stories of people who, like me, chose to observe rather than to lead, to listen rather than to speak.</p>
        </div>
        """
    },
    {
        "title": "Between the Lines: The Unwritten History of Digital Resistance (2006-2009)",
        "date": "2013-11-20",
        "tags": ["Digital Resistance", "Silent Protests", "Memory Preservation", "Human Dignity"],
        "content": """
        <div class="post-content">
        <p>There's a particular kind of courage that doesn't make the news. It's the courage of people who choose to document, to remember, to preserve what others would rather forget. In the mid-2000s, as governments around the world began to understand the power of digital surveillance, there emerged a quiet resistance movement that operated not through grand gestures, but through the careful preservation of truth.</p>
        
        <div class="quote">
        "I don't want to fight the system. I just want to make sure that when it's over, someone remembers what really happened." - A digital archivist, 2007
        </div>
        
        <p>I think about the librarians and archivists I've met over the years, people who understood that their role wasn't just to preserve books, but to preserve human dignity. In 2006, when WikiLeaks first appeared, it wasn't just about exposing secrets. It was about creating a space where truth could be preserved, even when powerful forces wanted it erased.</p>
        
        <h3>The Keepers of Memory:</h3>
        <ul>
        <li><strong>2006:</strong> The first digital preservation networks formed, often led by librarians and archivists</li>
        <li><strong>2007:</strong> Citizen journalists began using digital tools to document human rights abuses</li>
        <li><strong>2008:</strong> The emergence of "memory banks" - digital archives of personal testimonies</li>
        <li><strong>2009:</strong> Social media became a tool for preserving and sharing suppressed stories</li>
        </ul>
        
        <p>What strikes me most about this period is not the technological innovation, but the human determination to remember. People who had no formal training in activism or journalism found themselves becoming the chroniclers of their time. They documented not just the big events, but the small moments of human resilience that often go unnoticed.</p>
        
        <p>In my own work, I've come to understand that every library is a kind of resistance. Every book preserved, every story told, every voice remembered is a small act of defiance against the forces that would prefer silence. The digital age has given us new tools for this work, but the fundamental human impulse remains the same: to remember, to bear witness, to ensure that no voice is completely lost.</p>
        
        <p>Sometimes I think about my brother's letters from his military service. He never wrote about the grand strategy or the political implications of his work. He wrote about the people he met, the small moments of humanity he witnessed. In a way, that's what all of us are doing when we choose to document and preserve - we're writing letters to the future, ensuring that someone will remember what really happened.</p>
        </div>
        """
    },
    {
        "title": "The Quiet Revolution: When Silence Became a Form of Speech (2010-2013)",
        "date": "2013-10-08",
        "tags": ["Silent Revolution", "Digital Witnessing", "Human Stories", "Memory as Resistance"],
        "content": """
        <div class="post-content">
        <p>The years 2010-2013 taught us something profound about the nature of resistance. It wasn't always about speaking out. Sometimes it was about listening, about bearing witness, about refusing to forget. In an age of mass surveillance and digital control, the simple act of remembering became revolutionary.</p>
        
        <div class="quote">
        "Your memory is my final epitaph." - From a letter, 2013
        </div>
        
        <p>I think about the people who, during this period, chose to document rather than to protest, to preserve rather than to confront. They weren't the ones making headlines or giving speeches. They were the quiet observers, the careful record-keepers, the people who understood that sometimes the most powerful form of resistance is simply to remember.</p>
        
        <h3>The Witnesses:</h3>
        <ul>
        <li><strong>2010:</strong> Digital archives became tools for preserving suppressed histories</li>
        <li><strong>2011:</strong> Social media allowed ordinary people to document and share their experiences</li>
        <li><strong>2012:</strong> The emergence of "silent resistance" - using documentation as a form of protest</li>
        <li><strong>2013:</strong> The revelations about mass surveillance led to new forms of digital witnessing</li>
        </ul>
        
        <p>What I find most remarkable about this period is how it changed our understanding of what it means to be a witness. In the past, witnessing was something that happened to you - you were present at an event, and you remembered it. But in the digital age, witnessing became something you chose to do. You chose to document, to preserve, to remember.</p>
        
        <p>In my work at the library, I've seen how this shift has affected the way we think about history. It's no longer just about the big events and the famous people. It's about the small moments, the personal stories, the voices that might otherwise be lost. Every digital archive, every preserved memory, every documented experience is a testament to the human capacity for resilience and hope.</p>
        
        <p>Sometimes I think about the metal pieces my brother gives me when we meet. They're small, unremarkable things - a button from a uniform, a piece of shrapnel, a fragment of something larger. But each one tells a story, preserves a memory, bears witness to a moment that might otherwise be forgotten.</p>
        
        <p>Perhaps that's what all of us are doing in our own way - collecting fragments of truth, preserving moments of humanity, ensuring that the stories that matter don't disappear into silence. In a world that often seems determined to forget, remembering becomes an act of love, of resistance, of hope.</p>
        </div>
        """
    }
]

def main():
    # 侧边栏
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-content">
        <h3>📝 About the Author</h3>
        <p><strong>Measured Silence</strong></p>
        <p>A researcher and writer focused on human rights in the digital age. Specializing in the intersection of technology, privacy, and civil liberties from 2000-2013.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-content">
        <h3>🏷️ Categories</h3>
        <p><span class="tag">Silent Voices</span></p>
        <p><span class="tag">Digital Memory</span></p>
        <p><span class="tag">Human Stories</span></p>
        <p><span class="tag">Forgotten Histories</span></p>
        <p><span class="tag">Memory Preservation</span></p>
        <p><span class="tag">Digital Witnessing</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-content">
        <h3>📅 Archive</h3>
        <p>• December 2013</p>
        <p>• November 2013</p>
        <p>• October 2013</p>
        <p>• September 2013</p>
        </div>
        """, unsafe_allow_html=True)

    # 主内容区域
    st.markdown("""
    <div class="blog-header">
        <div class="blog-title">Do I Dare Disturb</div>
        <div class="blog-subtitle">A Chronicle of Human Rights in the Digital Age (2000-2013)</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 作者信息
    st.markdown("""
    <div class="author-info">
        <h3>✍️ Measured Silence</h3>
        <p>Welcome to my research blog exploring the complex relationship between human rights and digital technology during the pivotal years of 2000-2013. This period marked a fundamental shift in how we understand privacy, surveillance, and civil liberties in the digital age.</p>
        <p>Through careful analysis of documented cases, whistleblower revelations, and technological developments, I aim to provide a measured perspective on these critical years that shaped our current digital landscape.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 博客文章
    for i, post in enumerate(blog_posts):
        st.markdown(f"""
        <div class="blog-post">
            <div class="post-title">{post['title']}</div>
            <div class="post-meta">📅 {post['date']} | 📝 Measured Silence</div>
            <div class="post-content">
                {post['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 在文章之间添加分隔线
        if i < len(blog_posts) - 1:
            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # 页脚
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; font-size: 0.9rem; margin-top: 3rem;">
        <p>© 2013 Measured Silence. All rights reserved.</p>
        <p>This blog is dedicated to the memory of those who dared to disturb the silence.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
