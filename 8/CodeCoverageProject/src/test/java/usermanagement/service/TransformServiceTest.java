package usermanagement.service;

import org.junit.Before;
import org.junit.Test;
import usermanagement.entity.Person;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class TransformServiceTest {
    private static final String ALI = "Ali";
    private static final String ESLAMI = "Eslami";
    private static final String TEST_COMPANY = "Test";
    private static final Integer TEST_UID = 10;

    private TransformService transformer;

    @Before
    public void setup() {
        transformer = new TransformService();
    }

    @Test
    public void test_person_to_user() {

        Person person = new Person();
        person.setfName(ALI);
        person.setlName(ESLAMI);
        person.setCompanyName(TEST_COMPANY);
        person.setPersonId(TEST_UID);

        User user = transformer.toUserDomain(person);

        assertEquals(user.getFirstName(), person.getfName());
        assertEquals(user.getLastName(), person.getlName());
        assertEquals(user.getCompanyName(), person.getCompanyName());
        assertEquals(user.getUserId().intValue(), person.getPersonId());
    }

    @Test
    public void test_user_to_person() {
        User user = new User();
        user.setFirstName(ALI);
        user.setLastName(ESLAMI);
        user.setCompanyName(TEST_COMPANY);
        user.setUserId(TEST_UID);

        Person person = transformer.toUserEntity(user);
        assertEquals(user.getFirstName(), person.getfName());
        assertEquals(user.getLastName(), person.getlName());
        assertEquals(user.getCompanyName(), person.getCompanyName());
        assertEquals(user.getUserId().intValue(), person.getPersonId());
    }

    @Test
    public void test_twoway_validity() {

        User user = new User();
        user.setFirstName(ALI);
        user.setLastName(ESLAMI);
        user.setCompanyName(TEST_COMPANY);
        user.setUserId(TEST_UID);

        Person person = transformer.toUserEntity(user);
        User user_new = transformer.toUserDomain(person);

        assertEquals(user, user_new);
    }


}
